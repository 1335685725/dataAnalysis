import csv
import matplotlib.pyplot as plt
from _datetime import datetime


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # enumerate(iterable, start) 获取每个元素的索引和值, 索引从start开始， 默认为0
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 获取最高气温
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

    # print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red")
# 设置图形格式
plt.title('Daily high temperatures, 2014', fontsize=24)
plt.xlabel('', fontsize=16)
# 避免日期重叠， 让X坐标的时间倾斜
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()


