# 字段匹配，根据各表共有的关键字段，把各表所需的记录一一对应起来
# merge(x, y, left_on, right_on) -> DataFrame
# 参数说明 x第一个数据框，y第二个数据框，left_on第一个数据框用于匹配的列，right_on第二个数据框用于匹配的列
from pandas import read_csv
import pandas
items = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.12\data1.csv", sep="|", names=["id", "comments", "title"])


prices = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.12\data2.csv", sep="|", names=["id", "oldPrice", "nowPrice"])
# 默认只是保留链接上的部分
itemPrices = pandas.merge(items, prices, left_on="id", right_on="id")
print(itemPrices)
# 左链接
itemPrices = pandas.merge(items, prices, left_on="id", right_on="id", how="left")
# 右链接
itemPrices = pandas.merge(items, prices, left_on="id", right_on="id", how="right")
# 保留左右两边所有没有链接的部分
itemPrices = pandas.merge(items, prices, left_on="id", right_on="id", how="outer")
