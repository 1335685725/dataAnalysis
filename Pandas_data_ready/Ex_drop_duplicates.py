from pandas import DataFrame, read_csv

df = read_csv(r"C:\\Users\\Benlyons\\Desktop\\WorkSpace\\py\\dateanasisy\\4.3\\data.csv",)
# print(df)
# 找出重复的行
dIndex = df.duplicated()
# 根据某些列找出重复的值
# print(dIndex) # 返回是boolean类型
# 根据某些列， 找出重复数据
dIndex = df.duplicated("id")
# print(dIndex)
dIndex = df.duplicated(["id", "key"])
# 把重复数据提取出来
print(df[dIndex])
# 直接删除重复值，默认根据所有列进行删除
newDF = df.drop_duplicates()
print(newDF)
# 根据某一列进行删除
newDF = df.drop_duplicates("id")
print(newDF)





