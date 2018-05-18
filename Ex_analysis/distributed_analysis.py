# 分布分析,是在分组的基础上，将数据（定量）进行等距或者不等距的分组，进行研究各组分布规律的一种分析方法

import numpy
import pandas

data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\5.3\data.csv", encoding="utf-8")
# aggResult = data.groupby(by=["年龄"]).年龄.agg({"人数":numpy.size})
# print(aggResult)

bins = [min(data.年龄)-1, 20, 30, 40, max(data.年龄)+1]
labels = ["20岁以下", "21岁到30岁", "31岁到40岁", "40岁以上"]
data["年龄分层"] = pandas.cut(data.年龄, labels=labels, bins=bins)
aggResult = data.groupby(by=["年龄分层"]).年龄.agg({"人数":numpy.size})
print(aggResult)
pAggResult = round(aggResult/aggResult.sum(), 2)*100
print(pAggResult["人数"].map("{:.2f}%".format))