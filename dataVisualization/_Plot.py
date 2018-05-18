# 折线图：主要显示数据的变化趋势
# plot(x, y, style:画线的样式, color:画线的颜色, linewidth:线的宽度)
# title 图的标题

import pandas
import matplotlib
import matplotlib.pyplot as plt

data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\6.2\data.csv", encoding="utf-8")
# 对日期格式转化
data["购买日期"] = pandas.to_datetime(
    data["日期"]
)
main_color = (42/256, 87/256, 141/256, 1)

font = {"family": "SimHei", "size": 20}
matplotlib.rc("font", **font)
plt.xlabel("购买日期", color=main_color)
plt.ylabel("购买用户数", color=main_color)
plt.tick_params(axis="x", colors=main_color)
plt.tick_params(axis="y", colors=main_color)
# "-" 顺滑的曲线
plt.plot(data["购买日期"], data["购买用户数"], "-", color=main_color, linewidth=3)

plt.title("购买用户数量")
plt.show()
