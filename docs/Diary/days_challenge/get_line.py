import matplotlib.pyplot as plt
import os

date = '   24.12.19   '
index =    1

file_path = './docs/Diary/days_challenge/time_data.txt'
output_dir = './docs/Diary/days_challenge/charts'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 读取文件并解析数据
times = []
values = []

with open(file_path, 'r', encoding='utf-8') as file:  # 使用 utf-8 编码读取
    lines = file.readlines()
    
    i = 0  # 手动迭代行
    while i < len(lines):
        time_line = lines[i].strip()  # 获取时间行
        if not time_line:  # 跳过空行
            i += 1
            continue
        
        # 处理时间部分
        time_parts = time_line.split()
        if len(time_parts) >= 2:
            time_str = time_parts[1]  # 获取时间部分 "18:35:55"
            time_str = time_str[:5]  # 只保留前五个字符 "18:35"

            # 获取数值行
            value_line = lines[i + 1].strip() if i + 1 < len(lines) else ""  # 获取数值行（防止越界）
            if not value_line:  # 如果数值行为空，跳过
                i += 1
                continue

            try:
                value = int(value_line)  # 尝试将数值转换为整数
                times.append(time_str)  # 时间
                values.append(value)  # 数值
                # print(f"处理时间: {time_str}, 数值: {value}")
            except ValueError:
                print(f"无效的数值：{value_line}")  # 输出无效数据
        else:
            print(f"无效的时间格式：{time_line}")  # 输出格式错误的时间行

        i += 2  # 跳过当前处理的时间行和数值行

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(times, values, marker='o', linestyle='-', color='b')

# 设置图表标题和标签
plt.title('Time vs Scores on '+'{}'.format(date).strip()+'_{}'.format(index))
plt.xlabel('Time (HH:MM)')
plt.ylabel('Score')

# 设置纵轴范围为 0 到 5
plt.ylim(0, 5)

# 旋转X轴标签，以避免重叠
plt.xticks(rotation=45)

# 保存图表到指定目录
output_path = os.path.join(output_dir,'{}'.format(date).strip()+'_'+'{}'.format(index)+'_ts_line.png')
plt.tight_layout()  # 自动调整布局
plt.savefig(output_path)

# 显示图表
# plt.show()

# print(f"图表已保存到: {output_path}")
