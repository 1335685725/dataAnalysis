# 交叉分析，通常用于分析两个或两个以上，分组变量之间的关系，以交叉表的形式进行在变量间关系的对比分析
# 交叉计数函数：pivot_table(values:值, index：数据透视表中的行, columns列, aggfunc统计函数, fill_value ：NA值统一替换)

import pandas
import numpy

data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\5.4\data.csv", encoding="utf-8")
print(data)
bins = [min(data.年龄)-1, 20, 30, 40, max(data.年龄)+1]
labels = ["20岁以下", "21岁到30岁", "31岁到40岁", "40岁以上"]
data["年龄分层"] = pandas.cut(data.年龄, labels=labels, bins=bins)
ptResult = data.pivot_table(values=["年龄"], index=["年龄分层"], columns=["性别"], aggfunc=[numpy.size])
print(ptResult)