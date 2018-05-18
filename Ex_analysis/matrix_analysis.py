# 矩阵分析：是指根据食物，例如产品，服务等的两个重要属性（指标）作为分析的依据，进行关联分析，找出解决问题的一种分析方法

import pandas
import matplotlib
import matplotlib.pyplot as plt

mainColor = (42/256, 87/256, 141/256, 1);

# 设置字体
font = {"family": "SimHei", "size": 20}

matplotlib.rc("font", **font)

data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\5.8\data.csv", encoding="utf-8")

fig = plt.figure(figsize=(30, 20), dpi=80)

sp = fig.add_subplot(111)

# 设置坐标轴的范围
sp.set_xlim([0, data.GDP.max()*1.1])
sp.set_ylim([0, data.population.max()*1.1])
# 关闭坐标轴，坐标轴的刻度值
# sp.axis("off")
sp.get_xaxis().set_ticks([])
sp.get_yaxis().set_ticks([])
# 画点
sp.scatter(
    data.GDP, data.population, alpha=0.5, s=200,
    marker="o", edgecolor=mainColor, linewidths=5
)

# 画出均值线
sp.axvline(x=data.GDP.mean(), linewidth=1, color=mainColor)
sp.axhline(y=data.population.mean(), linewidth=1, color=mainColor)
sp.axvline(x=0, linewidth=3, color=mainColor)
sp.axhline(y=0, linewidth=3, color=mainColor)

sp.set_xlabel("GDP")
sp.set_ylabel("人口")

# 画标签
data.apply(
    lambda row: plt.text(
            row.GDP,
            row.population,
            row.province,
            fontsize=15
        ),
    axis=1
)
plt.show()