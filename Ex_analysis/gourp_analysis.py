# 分组分析,根据分组字段，将分析对象划分成不同部分，进行对比分析各组之间差异性的一种分析方法
# 常用的统计指标为计数，求和，平均值
# groupby(by=[分组列1，分组列2，。。。])[统计列1，统计列2，。。].agg([统计列别名1:统计函数1，统计列别名2:统计函数2，..])
import pandas
import numpy

data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\5.2\data.csv", encoding="utf-8")
# 古老版本，（已经不建议这样做了）
print(data.groupby(by=["class"]).score.agg({"总分":numpy.sum, "人数":numpy.size, "平均值":numpy.mean})
)
mean_score = data.groupby("class").score.mean()
print(type(mean_score))
print(pandas.Series(data.groupby("class").score.mean())
)
# 新版本,没找到官方解释，暂时不知道怎么对多列进行调用不同函数
print(data.score.groupby(by=data["class"]).sum().rename("总分"))