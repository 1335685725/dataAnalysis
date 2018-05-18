# 基本统计
# 常用的统计指标有计数，求和，平均，方差，标准差
# 描述性统计分析函数describe
import pandas


data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\5.1\data.csv", encoding="utf-8")
print(data.score.describe())
print(data.size)
print(data.score.size)
print(data.score.max())
print(data.score.min())
print(data.score.var())
print(data.score.sum())
print(data.score.std())
# 累计求和
print(data.score.cumsum())
# 求最大值和最小值所在的位置
print(data.score.idxmin())
print(data.score.idxmax())
# 百分位数的求解
print(data.score.quantile(
    0.3, interpolation="nearest"
))