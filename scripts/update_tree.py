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

if __name__ == "__main__":

    update_time = "2025.2.18"
    # yml文件内容注意正确缩进
    yml_content = """
    
  Diary: 
    - Diary/index.md
    - Reflection: 
      - exams: Diary/Reflection/exams.md
      - interview: Diary/Reflection/interview.md
      - Others: Diary/Reflection/Others.md
    - Research:
      - Comp: Diary/Research/comp1.md
      - Progress: Diary/Research/progress.md
      - Experience: Diary/Research/experience.md
    - Days_Challenge: 
      - Diary/days_challenge/index.md
      - '24.8': Diary/days_challenge/24.8.md
      - '24.10': Diary/days_challenge/24.10.md
      - '24.11': Diary/days_challenge/24.11.md
      - '24.12': Diary/days_challenge/24.12.md
      - '25.2': Diary/days_challenge/25.2.md
      - '25.2_2': Diary/days_challenge/25.2_2.md

    """
    root_re = re.compile(r'(\S*?):')
    root = root_re.findall(yml_content)[0]
    output_dir = f"./docs/{root}/"

    update_index(root, output_dir, yml_content, update_time)