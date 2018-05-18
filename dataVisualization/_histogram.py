# 直方图， 使用一系列等宽不等高的长方形来绘制，宽度表示数据范围的间隔，高度表示在给定间隔内的数据出现的频数
# 变化的高度形态表示数据的分布情况
# hist(x:需要进行绘制的向量, color:直方图填充的颜色, bins:设置直方图的分组个数, cumulative:设置是否累计计数=False)
import pandas
import matplotlib
import matplotlib.pyplot as plt

font = {"family": "Simhei"}

matplotlib.rc("font", **font)
data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\6.5\data.csv", encoding="utf-8")
print(data)

main_color = (42/256, 87/256, 141/256, 1)# 最后一位表示透明度s
plt.hist(data["购买用户数"], bins=20, color=main_color, cumulative=False)
plt.show()