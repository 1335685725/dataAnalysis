from pandas import DataFrame

df = DataFrame({
    'age': [21, 22, 23],
    'name': ["ken", "John", "JIMI"],
},index=["first", "second", "third"])
print(df)
print(df.ix[0:3,[0]])

# print(df)
# print("\n")
# print(df["age"])  # 按列访问
# print("\n")
# print(df[1:3])  # 按行访问
# print("\n")
# print(df.loc[["first", "second"]]) # loc进行多行访问
# print("\n")
# print(df.iloc[0:1, 0:2]) # 按行列号进行访问
# print("\n")
# print(df.at['first', 'name']) # 对应位置的值
# print("\n")
# print(df.columns) # 返回列
# df.columns = ['age2', 'name2']
# print(df.columns)
# print("\n")
# print(df.index) # 行索引
# print("\n")
# df.index = range(0, 3)
# print(df.index)
# print("\n")
# print(df)
# print("\n")
# df = df.drop(1, axis=0) # axis=0代表删除的是行，1为删除的是列
# print(df)
# df = df.drop("age2", axis=1) # 删除列
# print("\n")
# print(df)
# # print("\n")
# df.loc[len(df)] = [24, "kenken"] # 增加行， 这种方法效率非常低， 不应用于遍历中
# print("\n")
# print(df)
# df["newColumn"] = [2, 4, 6, 8]
# print(df)





