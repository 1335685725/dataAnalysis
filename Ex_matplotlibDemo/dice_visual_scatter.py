import matplotlib.pyplot as plt
from Ex_matplotlibDemo.die import Die

die1 = Die()
x_value = list(range(1, die1.num_sides+1))
results = []
for i in range(5000):
    result = die1.roll()
    results.append(result)
frequencies = []
for i in x_value:
    frequency = results.count(i)
    frequencies.append(frequency)
print(frequencies)
plt.scatter(x_value, frequencies, s=40, edgecolors=None, c='red')
plt.title("Results of dice rolling ", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Times", fontsize=14)
plt.axis([0, 7, 0, 1000])
plt.show()
