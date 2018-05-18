# 散点图,用分布状态反应变量间关系的一种图形
# plot(x,y,".", color=(r, g, b))

import pandas
import matplotlib
import matplotlib.pyplot as plt

data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\6.1\data.csv", encoding="utf-8")
main_color = (42/256, 87/256, 141/256, 1)# 最后一位表示透明度s
font = {"family": "SimHei", "size": 20}
matplotlib.rc("font", **font)
plt.xlabel("广告费用", color=main_color)
plt.ylabel("购买用户数", color=main_color)
plt.tick_params(axis="x", colors=main_color)
plt.tick_params(axis="y", colors=main_color)

plt.plot(data["广告费用"], data["购买用户数"], ".", color=main_color, linewidth=3)
plt.show()