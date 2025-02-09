import plotly.graph_objects as go
import pandas as pd
import re

def get_diff(h1,m1,h2,m2):
    h1 = h1 if h1>2 else h1+24
    h2 = h2 if h2>2 else h2+24
    return (h2-h1)*60 + (m2-m1)

def get_mid(h1,m1,h2,m2):
    h1 = h1 if h1>2 else h1+24
    h2 = h2 if h2>2 else h2+24
    half_diff = round(get_diff(h1,m1,h2,m2)/2)
    h = h1+half_diff//60
    m = m1+half_diff%60
    return f'{h}:{m}'

input_dir = r'D:\desktop\Blog\docs\Diary\days_challenge\timedata.txt'
output_dir = r'D:\desktop\Blog\docs\Diary\days_challenge\\'
re_time = re.compile(r'(\d{2}):(\d{2}):\d{2}')

file = open(input_dir, 'r',encoding='utf-8')
text = file.readlines()
file.close()

times_list = []
things_list = []

for i in text:
    times = (re_time.findall(i))
    if times:
        hours = int(times[0][0])
        mins = int(times[0][1])
        times[0]=(hours,mins)
        
        times_list.extend(times)
        continue
    elif i.strip():
        things_list.append(i.strip())
        
# seen = set()
# times_list = [x for x in times_list if not (x in seen or seen.add(x))]
times_list = times_list[::2]
diff_list = [get_diff(*times_list[i],*times_list[i+1]) for i in range(0,len(times_list)-1)]
mid_list = [get_mid(*times_list[i],*times_list[i+1]) for i in range(0,len(times_list)-1)]

date = things_list.pop(0)  # 去除第一行（标记开始）

scores_list = [float(i) for i in things_list[1::2]]
things_list = things_list[::2]

# print(times_list,len(times_list))
# print(diff_list,len(diff_list))
# print(mid_list,len(mid_list))
# print(scores_list,len(scores_list))
# print(things_list,len(things_list))
# print(date)

df = pd.DataFrame({'diff':diff_list,'mid':mid_list,'scores':scores_list,'things':things_list})

trace1 = go.Bar(x=df['mid'],y=df['diff'],text=df['things'],name='活动时长/min',
                marker_color='LightSteelBlue',
                hovertemplate='Mid: %{x}<br>时长: %{y} min<br>内容: %{text}<extra></extra>',
                textposition='none')
trace2 = go.Scatter(x=df['mid'],y=df['scores'],text=df['diff'],name='负熵值',
                    marker_color='lightgreen',yaxis='y2',
                    mode='lines+markers',
                    hovertemplate='Mid: %{x}<br>时长: %{text} min<br>负熵值: %{y}<extra></extra>',
                    )


data = [trace1,trace2]

layout = go.Layout(
    title='今日活动时长与负熵值',
    xaxis=dict(title='活动时刻中值'),
    yaxis=dict(title='活动时长/min'),
    yaxis2=dict(title='负熵值',
                overlaying='y',
                range=[0, 4],
                side='right')
)

fig = go.Figure(data=data,layout=layout)
fig.write_html(output_dir + f'bar-25.{date}.html',include_plotlyjs="cdn", full_html=False)

# fig.show()
