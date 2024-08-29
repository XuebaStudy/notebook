import matplotlib.pyplot as plt  
import re  
# from collections import defaultdict  
from matplotlib import rcParams
config = {
        "font.family": 'serif',
        "mathtext.fontset": 'stix',  # matplotlib渲染数学字体时使用的字体，和Times New Roman差别不大
        "font.serif": ['FZYaoti'],
        'axes.unicode_minus': False  # 处理负号，即-号
    }
rcParams.update(config)

date = "24.8.15"
data = """  
晨跑/normal/10min
晨读/C1SC/30min
背单词/review40/8min
学物理/C4S1/55min
学物理/C4S2&C4S3(Q)/15min
计科导/C13&C14(Q)/20min
背单词/R29N20/20min
探索/mkdocs&latex/170min
探索/latex/180min
探索/visualization/115min
"""  
  
# 定义固定颜色映射  
activity_colors = {  
    '晨跑': 'tab:blue',  
    '晨读': 'tab:orange',  
    '背单词': 'tab:green',  
    '学物理': 'tab:red',  
    '计科导': 'tab:purple',  
    '探索': 'tab:cyan',  
}  
  
# 解析数据  
activities = []  
time_spent = []  
  
# 正则表达式  
pattern = r'(.+?)/(.+?)/(\d+)min'  
  
for line in data.strip().split('\n'):  
    match = re.match(pattern, line)  
    if match:  
        main_activity = match.group(1)  
        minutes = int(match.group(3))  
          
        # 合并主活动和子活动为标签（如果需要）  
        label = f"{main_activity} ({match.group(2)})"  
        activities.append(label)  
        time_spent.append(minutes)  
  
# 创建饼状图，使用固定颜色  
fig, ax = plt.subplots()  
wedges, texts, autotexts = ax.pie(time_spent, labels=activities, autopct='%1.1f%%',
  startangle=90, colors=[activity_colors[a.split(' (')[0]] for a in activities],  
  pctdistance=0.85,labeldistance=1.1)
  
# 自定义标签和百分比的外观  
for text in texts:  
    text.set_color('black')  
    text.set_fontsize(10)  
for autotext in autotexts:  
    autotext.set_color('black')  
    autotext.set_fontsize(8)  
  
ax.axis('equal')  # 确保饼状图是圆形  
plt.savefig("./docs/Diary/14_days_challenge/charts/pie-{}.png".format(date),)
# 显示图表  
# plt.show()