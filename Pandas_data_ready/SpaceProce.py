# 空格值处理
from pandas import read_csv

df = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.5\data.csv")
# print(df)
# 清除字符串左边的数据
newName = df['name'].str.lstrip()
# print(newName)
# 清除字符串右边的数据
newName = df['name'].str.rstrip()
# print(newName)
# 清除字符串左右两边的数据
newName = df['name'].str.strip()
# print(newName)
# 重新赋值给df变量
df['name'] = newName
