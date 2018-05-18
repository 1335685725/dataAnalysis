from random import choice
import matplotlib.pyplot as plt


class RandomWalk:
    '''一个生成随机漫步的类'''

    def __init__(self, num_point=5000):
        '''初始化随机漫步的属性'''
        self.num_point = num_point

        # 所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''计算随机漫步包含的所有点'''
        # 不断漫步直到达到列表达到指定的长度
        while len(self.x_values) < self.num_point:
            # 决定前进方向以及沿这个方向前进的距离
            # 拒绝原地踏步
            x_step = get_step()
            y_step = get_step()
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def show_view(self, s=15, c="reds", cmap="", linewidth=5):
        plt.figure(figsize=(10, 6), dpi=128)
        # plt.scatter(self.x_values, self.y_values, s=s, c=c, cmap=cmap)
        plt.plot(self.x_values, self.y_values, linewidth=linewidth)
        # 隐藏坐标轴
        # plt.axes().get_xaxis().set_visible(False)
        # plt.axes().get_yaxis().set_visible(False)
        plt.show()


def get_step():
    direction = choice([-1, 1])
    distance = choice([0, 1, 2, 3, 4])
    step = direction * distance
    return step

# 模拟多次随机漫步
fw = RandomWalk()
while True:
    fw.__init__()
    fw.fill_walk()
    # point_numbers = list(range(fw.num_point))
    # fw.show_view(s=1, c=point_numbers, cmap=plt.cm.Blues, linewidth=3)
    fw.show_view(linewidth=3)
    keep_running = input("keep running? y/n \n")
    if keep_running == "n":
        print("end")
        break

