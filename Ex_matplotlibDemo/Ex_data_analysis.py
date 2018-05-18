import matplotlib.pyplot as plt


# Ex15-1 | 2
'''绘制平方函数散点图， 并且颜色映射渐变'''
x_value = list(range(1001))
y_value = [x**3 for x in x_value]
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds, edgecolors=None, s=40)
plt.xlabel("value", fontsize=14)
plt.ylabel("value**3", fontsize=14)
plt.title("Title", fontsize=24)
plt.axis([0, 1100, 0, 1100000000])
plt.show()

# Ex15-3
from Ex_matplotlibDemo import Demo_randomWalk
fw = Demo_randomWalk.RandomWalk()
while True:
    # fw.__init__(50000)
    fw.fill_walk()
    # point_numbers = list(range(fw.num_point))
    # fw.show_view(s=1, c=point_numbers, cmap=plt.cm.Blues, linewidth=3)
    fw.show_view(linewidth=3)
    keep_running = input("keep running? y/n \n")
    if keep_running == "n":
        print("end")
        break


