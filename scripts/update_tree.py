import yaml
import re
from get_index import generate_markdown

def update_index(root, output_dir, yml_content, update_time):
    """仅更改原 index.md 中 Contents Tree 部分的内容, 直到 >Latest update time: 的那一行为止"""

    # 直接解析 YAML 字符串
    data = yaml.safe_load(yml_content)

    markdown = generate_markdown(root, data[root])
    markdown += f"\n\t>Latest update time: {update_time}"

    re_tree = re.compile(r'"Contents Tree"\n(.*?>Latest update time:.*?)\n', re.DOTALL)
    # 写入输出文件
    with open(output_dir + 'index.md', 'r+', encoding='utf-8') as file:
        contents = file.read()
        new_contents = contents.replace(re_tree.search(contents).group(1), markdown)
        file.truncate(0)
        file.seek(0)
        file.write(new_contents)


def update_all_indexes(yml_content, update_time, base_output_dir="./docs/"):
    """根据 YAML 内容更新所有部分的 index.md 文件"""
    data = yaml.safe_load(yml_content)
    for root in data.keys():
        output_dir = f"{base_output_dir}{root}/"
        update_index(root, output_dir, yml_content, update_time)


if __name__ == "__main__":

    update_time = "2025.4.16"

    base_output_dir="./docs/" 

    # yml文件内容注意正确缩进（且根级部分前没有"-"）
    yml_content = """
    
  Diary: 
    - Diary/index.md
    - Reflection: 
      - exams: Diary/Reflection/exams.md
      - interview: Diary/Reflection/interview.md
      - others: Diary/Reflection/Others.md
    - Research:
      - 星伴明行: Diary/Research/comp1.md
      - progress: Diary/Research/progress.md
      - experience: Diary/Research/experience.md
    - Days_Challenge: 
      - Diary/days_challenge/index.md
    - Thinking:
      - Diary/Thinking/index.md
      - '24.12.5': Diary/Thinking/24.12.5.md
      - 'Things' : Diary/Thinking/things.md
      
    """

    update_all_indexes(yml_content, update_time, base_output_dir)