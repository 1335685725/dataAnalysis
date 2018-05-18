import matplotlib.pyplot as plt


x_value = list(range(1001))
y_value = [x**2 for x in x_value]
plt.scatter(x_value, y_value, s=40, edgecolors=None, c=y_value, cmap=plt.cm.Blues)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square value", fontsize=14)
# 坐标轴取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()

