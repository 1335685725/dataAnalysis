# 数据分组，根据数据分析对象的特征，按照一定的数值指标，把数据分析对象划分为不同区间进行研究，以揭示其内在联系和规律性
# cut(series, bins, right=True, label=NULL)
# series需要分组的数据,bins分组的划分数组,right右边是否闭合，labels 自定义标签
import pandas
data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.15\data.csv", sep="|")
# 分组区间
bins = [
    min(data.cost)-1, 20, 40, 60, 80, 100, max(data.cost)+1
]
data["cut"] = pandas.cut(data.cost, bins)
#
data["cut"] = pandas.cut(data.cost, bins, right=False)
#分组标签
labels = ["20以下", "20到40", "40到60", "60到80", "80到100", "100以上"]

data["cut"] = pandas.cut(data.cost, bins, right=False, labels=labels)
print(data)