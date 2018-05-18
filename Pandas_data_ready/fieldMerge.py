# 字段合并
import pandas
from pandas import read_csv

df = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.11\data.csv", sep=" ", names=["band", "area", "num"])
print(df)
df = df.astype(str)

tel = df["band"] + df["area"] + df["num"]

df["tel"] = tel
print(df)