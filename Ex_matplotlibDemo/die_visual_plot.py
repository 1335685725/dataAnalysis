import matplotlib.pyplot as plt
from Ex_matplotlibDemo.die import Die

die = Die()
input_value = list(range(1, die.num_sides+1))
print(input_value)
results = []
for i in range(50000):
    result = die.roll()
    results.append(result)
frequencies = []
for i in range(1, die.num_sides+1):
    frequency = results.count(i)
    frequencies.append(frequency)
print(frequencies)
plt.plot(input_value, frequencies, linewidth=5)
plt.title("A_TITLE", fontsize=24)
plt.xlabel("X_LABEL", fontsize=14)
plt.xlabel("Y_LABEL", fontsize=14)
# 设置刻度标记
plt.tick_params(axis="both", labelsize=14)
plt.show()
