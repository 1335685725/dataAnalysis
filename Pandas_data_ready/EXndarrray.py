import numpy

# 创建一维数组
x = numpy.array([(1, 2, 3), (1, 2, 3)])
print(x)
print(x.ndim)
print(x.size)
print(x.shape)
print(x[0:2, 0:2])
print(x.sum(axis=1))
#方差
x.var()
#标准差
x.std()
for row in x:
    print(row)
b = x.reshape(3, 2) # x不变
c = x.resize(3, 2) # x变
print(b)
# 创建一维数组， 和range很像， 不过可以处理浮点数

float_nums = numpy.arange(1, 5, 0.5)

print(float_nums)
# a_array = numpy.ndarray()
# print(a_array)
# b_array = numpy.ndarray([1, 2, 3,], [4, 5, 6])
# print(b_array)
# 创建随机数
a_random = numpy.random.random()
print(a_random)
# 创建等差数组, 包含end
lin = numpy.linspace(1, 50, 25, dtype=int)
# print(lin)
# 从一个函数创建某一个一维数组
# ff = numpy.fromfunction(lambda i, j: (i + 1)*(j + 1), (9*9))
"da s d".split(" ")
