from Ex_PygalDemo.die import Die
import pygal

# 创建两个骰子
die_1 = Die()
die_2 = Die()
# 投掷骰子多次， 并将结果存入一个列表中去
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# 分析结果
frequencies = []
max_result = die_2.num_sides + die_1.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = [str(i) for i in range(2, 13)]
hist.x_title = "Results"
hist.y_title = "Frequency of Result"
hist.add("D6 + D6", frequencies)
hist.render_to_file("dice_visual.svg")




