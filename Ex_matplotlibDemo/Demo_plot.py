import matplotlib.pyplot as plt
# input_value = list(range(1, 6))
input_value = [1, 2, 3, 4, 5]
squares = [value**2 for value in input_value]
print(input_value)
print(squares)

plt.plot(input_value, squares, linewidth=5)
plt.title("A_TITLE", fontsize=24)
plt.xlabel("X_LABEL", fontsize=14)
plt.xlabel("Y_LABEL", fontsize=14)
# 设置刻度标记
plt.tick_params(axis="both", labelsize=14)
plt.show()
