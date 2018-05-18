# 字段抽取
# 使用slice（start， stop） 开始位置和结束位置
from pandas import read_csv
import functools.map

df = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.6\data.csv")

df["tel"] = df["tel"].astype(str)

# 运营商
bands = df["tel"].str.slice(0, 3)
# print(bands)
# 地区
areas = df["tel"].str.slice(3, 7)
# print(areas)
# 号码段
nums = df["tel"].str.slice(7, 11)
# print(nums)
map()
# 赋值回去
df['bands'] = bands
df['areas'] = areas
df['nums'] = nums