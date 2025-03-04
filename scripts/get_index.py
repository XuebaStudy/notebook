import yaml
import re

def generate_markdown(root, data, prefix="    "):
    markdown = ""
    if isinstance(data, dict):  # 如果是字典
        for key, value in data.items():
            if isinstance(value, dict) or isinstance(value, list):  # 如果值是字典或列表
                # 检查是否存在 index.md 文件
                has_index = False
                
                if isinstance(value, dict):
                    has_index = any(v.endswith("index.md") for v in value.values() if isinstance(v, str))
                elif isinstance(value, list):
                    index_path = [item for item in value if isinstance(item, str) and item.endswith("index.md")]
                    has_index = any(index_path)
                # 如果存在 index.md 文件，则生成外层目录链接
                if has_index:
                    clean_path = index_path[0].replace(f"{root}/", "")
                    markdown += f"{prefix}- [{key}]({clean_path})\n"
                else:
                    # 如果不存在 index.md 文件，则只显示目录名
                    markdown += f"{prefix}- {key}\n"
                # 递归处理内层内容，缩进增加 4 个字符
                markdown += generate_markdown(root, value, prefix + "    ")
            else:  # 如果值是字符串（文件路径）
                # 去掉路径中的 "root/" 前缀
                clean_path = value.replace(f"{root}/", "")
                # 获取文件名作为链接文本
                link_text = key
                markdown += f"{prefix}- [{link_text}]({clean_path})\n"
    elif isinstance(data, list):  # 如果是列表
        for item in data:
            if isinstance(item, dict):  # 如果列表中的项是字典
                markdown += generate_markdown(root, item, prefix)
            else:  # 如果列表中的项是字符串（文件路径）
                # 去掉路径中的 "root/" 前缀
                clean_path = item.replace(f"{root}/", "")
                # 获取文件名作为链接文本
                link_text = item.split('/')[-1].replace('.md', '')
                # 如果文件名是 index.md，则跳过（因为外层目录已经生成链接）
                if link_text == "index":
                    continue
                markdown += f"{prefix}- [{link_text}]({clean_path})\n"
    return markdown

def get_index(root, output_dir, yml_content, update_time):
    """生成格式化的 index.md 文件"""

    # 直接解析 YAML 字符串
    data = yaml.safe_load(yml_content)

    # 生成 Markdown 内容
    # markdown = f"# {root}\n\n!!! abstract\n\t\t\n\n## Contents Tree\n"
    markdown = f'# {root}\n\n!!! abstract\n\t\n\n!!! info "Contents Tree"\n'
    markdown += generate_markdown(root, data[root])
    markdown += f"\n\t>Latest update time: {update_time}\n\n"

    # 写入输出文件
    with open(output_dir + 'index.md', 'w', encoding='utf-8') as file:
        file.write(markdown)

if __name__ == "__main__":
    # 千万小心这是覆盖写，原index.md会丢失！！！
    update_time = "2025.3.4"

    # yml文件内容注意正确缩进
    yml_content = """
    
Belief:  
    - Belief/index.md
    - charators: 
      - 灰之魔女伊蕾娜: Belief/charactors/灰之魔女伊蕾娜.md
      - 洛琪希: Belief/charactors/洛琪希.md
    - sentences: Belief/sentences.md

    """
    root_re = re.compile(r'(\S*?):')
    root = root_re.findall(yml_content)[0]
    output_dir = f"./docs/{root}/"

    get_index(root, output_dir, yml_content, update_time)