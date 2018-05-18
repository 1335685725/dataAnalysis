import csv
import matplotlib.pyplot as plt
from _datetime import datetime
import matplotlib as mpl


filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # enumerate(iterable, start) 获取每个元素的索引和值, 索引从start开始， 默认为0
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 获取最高气温
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)
    # 根据数据绘制图形
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c="red", alpha=0.5) # alpha越接近0 越透明 0表示完全透明
    plt.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1 )
    plt.title("最高气温和最低气温 -2014", fontsize=24)
    plt.xlabel("", )
    plt.ylabel("Temperature (F)")
    plt.tick_params(axis="both", which="major", labelsize=16)
    fig.autofmt_xdate()
    plt.show()






