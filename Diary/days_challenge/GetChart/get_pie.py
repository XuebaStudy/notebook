# 定义固定颜色映射  
activity_colors = {  
    '概率论': 'tab:green',  
    'pytorch': 'tab:orange',  
    'CET': 'tab:purple',  
    '数值分析': 'tab:brown',  
    '计组': 'tab:blue',  
    '科研': 'tab:cyan', 
    '休息': '#A9A9A9' ,
    '小提琴':'#D2691E',
    '乐团':  '#D2691E',
    '上课': '#696969',
    'AI导':'#48D1CC',
    '运动':'#FFA500',
    'ADS':'#6B8E23',
    '事务':'#808080',   # Gray
    '物理':'#1E90FF',   # DodgerBlue
    '整理':'#DCDCDC',   # Gainsboro
    '博客':'#DCDCDC',
    
    # '上课&背单词':'#6A5ACD',  # SlateBlue
    # '上课&AI导':'#6A5ACD'
}  

from date_data import *
import matplotlib.pyplot as plt  
import re   
from matplotlib import rcParams
config = {
        "font.family": 'serif',
        "mathtext.fontset": 'stix',  # matplotlib渲染数学字体时使用的字体，和Times New Roman差别不大
        "font.serif": ['FZYaoti'],
        'axes.unicode_minus': False  # 处理负号，即-号
    }
rcParams.update(config)
  
# 解析数据  
activities = []  
time_spent = []  
  
# 正则表达式  
pattern = r'(.+?)/(.+?)/(\d+)min/(\d+)'  

score_sum = 0 
for line in data.strip().split('\n'):  
    match = re.match(pattern, line)  
    if match:  
        main_activity = match.group(1)  
        minutes = int(match.group(3))
        scores = int(match.group(4))  
          
        # 合并主活动和子活动为标签（如果需要）  
        label = f"{main_activity} ({match.group(2)})"  
        activities.append(label)  
        time_spent.append(minutes)
        
        score_sum += scores * minutes  
  
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

se_min=60*(e_h-s_h)+(e_m-s_m)
print('今日加权有效时长:',score_sum//60,'h',score_sum%60,'min')
print('今日时间相对利用比: {:.2f} %'.format(score_sum/se_min*100))