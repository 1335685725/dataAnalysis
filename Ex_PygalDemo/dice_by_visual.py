import pygal
from Ex_PygalDemo.die import Die

die_1 = Die()
die_2 = Die()
max_result = die_1.num_sides * die_2.num_sides
results = []
for num in range(5000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
# 生成结果列表
res = []
for i in range(1, 7):
    for j in range(1, 7):
        x = i * j
        if x not in res:
            res.append(x)
res.sort()
frequencies = []
for i in res:
    frequency = results.count(i)
    frequencies.append(frequency)
str_res = [str(x) for x in res]
print(str_res)
hist = pygal.Bar()
hist.title = "Results of two dice point by"
hist.x_labels = res
hist.x_title = "Results"
hist.y_title = "Frequency of Result"
hist.add("D6 * D6", frequencies)
# hist.render()
hist.render_to_file("dice_by_visual.svg")



