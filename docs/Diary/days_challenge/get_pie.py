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

date = "24.10.2"
data = """  
概率论/N2.3&H2.1/70min
背单词/R80/25min
数值分析/R6.n/25min
休闲/biliblili/80min
数值分析/R6.n/60min
数值分析/Lab3/40min
午休/NM/25min
ADS/team-work/30min
事务/scholarship/30min
运动/NM/40min
科研/RP/135min
AI导/Lab2/100min
总结/blog/20min
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
    '总结': '#696969',
    'AI导':'#48D1CC',
    '运动':'#FFA500',
    'ADS':'#6B8E23',
    '事务':'#808080'    # Gray
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