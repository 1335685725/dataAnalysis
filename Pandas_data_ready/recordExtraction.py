# 记录抽取
# 比较运算 df[df.comments >10000];
# 范围运算 df[df.comments.between(1000, 10000)], 这里的1000和10000都包含在里边
# 空值匹配 df[pandas.isnull(df.title)]
# 字符匹配 df[df.title.str.contains('台电', na=False)]， na是指空值的处理方式，False不匹配
# 逻辑运算 df[(df.comments>=1000)&(df.comments<=10000)] 与(&),或(|)，取反(not)
import pandas
df = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.8\data.csv", sep="|")
# 单条件
df = df[df.comments>10000]
# print(df)
# 多条件
df = df[df.comments.between(1000, 10000)]
# print(df)
# 过滤空值所在的行
df = df[pandas.isnull(df.title)]
# print(df)
# 根据关键字进行过滤
df = df[df.title.str.contains("台电", na=False)]
# print(df)
# ~表示取反
df = df[~df.title.str.contains("台电", na = False)]
# print(df)
# 组合逻辑运算
df = df[(df.comments>=1000)&(df.comments<=10000)]
# df = df[df.comments]
print(type(df))
print(df)








