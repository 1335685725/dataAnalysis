# 记录合并函数 concat([DataFrame1, DataFrame2,...])
import pandas
from pandas import read_csv

data1 = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.10\data1.csv", sep="|")
data2 = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.10\data2.csv", sep="|")
data3 = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.10\data3.csv", sep="|")

# data = pandas.concat([data1, data2, data3])
# print(data)
# print(data1)
# print(data2)
# print(data3)
print(data1.loc[[0, 1],["id"]])
print(type(data1.loc[[0, 1],["id"]]))
data = pandas.concat([
    data1.loc[:, ["id", "comments"]],
    data2.loc[:, ["id", "title"]],
    data3.loc[:, ["comments", "title"]]
])
print(data)