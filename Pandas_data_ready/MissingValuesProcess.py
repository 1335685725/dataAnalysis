from pandas import read_csv
# 把文件中的a和b当作NaN处理
df = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.4\data2.csv", na_values=["a", "b"])
# print(df)
#找出空值所在位置
isNA = df.isnull()
# print(isNA)
# 找出空值所在的行
print(df[isNA.any(axis=1)]) #针对所有的列
#
print(df[isNA[["key"]].any(axis=1)]) # 针对key这一列
#
df[isNA[["key", "value"]].any(axis=1)]
# 填充NaN值为“未知”
df = df.fillna("未知")
# print(df)
# 直接删除空值所在的行
newDF = df.dropna()
print(newDF)