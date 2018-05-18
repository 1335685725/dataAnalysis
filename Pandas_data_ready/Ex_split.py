# 字段拆分
# split(seq, n, expand=False) ,sql是分割符， n是分割成多少列返回， expand是否以DataFrame形式返回， False时 返回Series
from pandas import read_csv
df = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.7\data.csv")
# 分成两列
newDF = df['name'].str.split(' ', 1, True)
print(newDF)

newDF.columns = ['band', 'name']



