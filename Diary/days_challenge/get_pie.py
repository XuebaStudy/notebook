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

date = "24.11.6"
data = """  
背单词/R60/20min
上课/physics/100min
博客/new css/25min
计组/Lab4/120min
休息/noon break/60min
ADS/HW/95min
运动/NM/40min
背单词/R100/25min
计组/HW/70min
博客/Music/25min
科研/read paper/80min
概率论/HW/30min
概率论/review/35min
博客/conclusion/20min
"""  
  
# 定义固定颜色映射  
activity_colors = {  
    '概率论': 'tab:green',  
    'pytorch': 'tab:orange',  
    '背单词': 'tab:purple',  
    '数值分析': 'tab:brown',  
    '计组': 'tab:blue',  
    '科研': 'tab:cyan', 
    '午休': '#A9A9A9' ,
    '休闲': '#A9A9A9' ,
    '休息': '#A9A9A9' ,
    '小提琴':'#D2691E',
    '上课': '#696969',
    'AI导':'#48D1CC',
    '运动':'#FFA500',
    'ADS':'#6B8E23',
    '事务':'#808080',   # Gray
    '普物':'#1E90FF',   # DodgerBlue
    '整理':'#DCDCDC',   # Gainsboro
    '博客':'#DCDCDC'
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