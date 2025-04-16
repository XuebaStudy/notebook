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
    
  Lesson: 
    - Lesson/index.md
    - NJU ISC PA: Lesson/NJU ISC PA/Tasks.md
    - Learning Path (in ZJU): Lesson/How_1.md
    - Math:
      - 常微分方程: Lesson/Math/ODE/note.md

  Code: 
    - Code/index.md
    - C++: Code/C++/Cpp_note.md
    - Python:
      - matplotlib.pyplot: Code/Python/matplotlib.pyplot/1.md
      - Mix:
        - req_re_df_1: Code/Python/Mix/req_re_df_250209.md
    - CUMCM:
      - Code/CUMCM/index.md
      - 2020年 A题: Code/CUMCM/20A.md
    - Regex (正则表达式): Code/Regex.md

  Research:
    - Research/index.md
    - 3DGS: 
      - 3D Gaussian Splatting for Real-Time Radiance Field Rendering: Research/3DGS/1.md
    - Quantization:
      - (Survey) Model Quantization for DNN in Image Classification: Research/Quantization/1.md
      - (Survey) Model Quantization and Hardware Acceleration for Vision Transformers: Research/Quantization/2.md
    - Paper Tips: Research/paper_tips.md

  Music:
    - Music/index.md
    - Music with places:
      - Music/places/index.md
    - Others: 
      - mp3->mp4 (有声频谱): Music/Others/mp3_visualization.md

  Tool:
    - Tool/index.md
    - Mkdocs: 
      - Commands: Tool/mkdocs/commands.md
      - Others: Tool/mkdocs/others.md
    - Linux:
      - Terminal: Tool/Linux/commands.md
      - 基本配置: Tool/Linux/Linux_setup.md
      - Vim: 
        - Tool/Linux/Vim/tips.md
      - Others: Tool/Linux/others.md
    - Git: Tool/git.md
    - Adobe:
      - PS shortcuts: Tool/Adobe/PS_shortcut.md
    - Others: 
      - Terminal:如何使"命令"显示在"路径"下一行: Tool/Others/terminal_1.md

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
      - '24.8': Diary/days_challenge/24.8.md
      - '24.10': Diary/days_challenge/24.10.md
      - '24.11': Diary/days_challenge/24.11.md
      - '24.12': Diary/days_challenge/24.12.md
      - '25.2': Diary/days_challenge/25.2.md
      - '25.2~3': Diary/days_challenge/25.2_2.md
      - '25.4': Diary/days_challenge/25.4.md
    - Thinking:
      - Diary/Thinking/index.md
      - '24.12.5': Diary/Thinking/24.12.5.md
      - 'Things' : Diary/Thinking/things.md

  Belief:  
    - Belief/index.md
    - charators: 
      - 灰之魔女伊蕾娜: Belief/charactors/灰之魔女伊蕾娜.md
      - 洛琪希: Belief/charactors/洛琪希.md
    - sentences: Belief/sentences.md

    """

    update_all_indexes(yml_content, update_time, base_output_dir)