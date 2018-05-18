from pandas import Series

s = Series(
    ['a', True, 1]
)
x = Series(
    ['a', True, 1],
    index=["first", "second", "third"]
)
# print(x[1])
# print(x["second"])
# 不能追加列表 只能追加pd.Series 和 pd.DataFrame pa.Panel
# x.append(["2"])
n = Series(['2'])
x.append(n)
print(x)
print("\n")
x = x.append(n)
print(x)
# 索引定义过后， 新的索引从0开始
print("\n")
print("2" in x) # False
print("2" in x.values) # True

print("\n")
print(x[1:3])
print("\n")
print(x[[0, 2, 1]]) # 按照索引输入的顺序返回一个Series对象
print("\n")
# 根据索引进行删除
x.drop(0)
x = x.drop("first")
x = x.drop(x.index[2]) # drop返回一个Series对象， 需要重新赋值才可以删除
print(x)
print("\n")
x = x[1 != x.values]   # 1 和 True都会删除， 因为他们的hash和value都相同
print(x)