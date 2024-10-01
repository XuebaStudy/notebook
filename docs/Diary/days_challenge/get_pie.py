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

date = "24.10.1"
data = """  
概率论/R2.1&2.2/60min
背单词/R70/25min
计组/Lab1-report/65min
科研/RP/40min
科研/RP/35min
pytorch学习/-2.1/45min
背单词/R74/25min
午休/TL/210min
数值分析/R2.2(LE)/50min
科研/RP/25min
背单词/N60/20min
小提琴/Free/90min
休闲/bilibili/150min
数值分析/R2.3-2.6/25min
总结/blog/30min
"""  
  
# 定义固定颜色映射  
activity_colors = {  
    '概率论': 'tab:green',  
    'pytorch学习': 'tab:orange',  
    '背单词': 'tab:purple',  
    '数值分析': 'tab:brown',  
    '计组': 'tab:blue',  
    '科研': 'tab:cyan', 
    '午休': '#A9A9A9' ,
    '休闲': '#A9A9A9' ,
    '休息': '#A9A9A9' ,
    '小提琴':'#D2691E',
    '总结': '#696969'
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
plt.savefig("./docs/Diary/days_challenge/charts/pie-{}.png".format(date),)
# 显示图表  
# plt.show()