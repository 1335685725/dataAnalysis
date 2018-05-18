# 结构分析,实在分组以及交叉的基础上，计算各组成部分所占的比重，进而分析总体的内部特征的一种分析方法
# 参数axis说明:0按列运算，1按行计算
#
import pandas
import numpy

data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\5.4\data.csv", encoding="utf-8")

bins = [min(data.年龄)-1, 20, 30, 40, max(data.年龄)+1]
labels = ["20岁以下", "21岁到30岁", "31岁到40岁", "40岁以上"]
data["年龄分层"] = pandas.cut(data.年龄, labels=labels, bins=bins)
ptResult = data.pivot_table(values=["年龄"], index=["年龄分层"], columns=["性别"], aggfunc=[numpy.size])
# print(ptResult)
print(ptResult.sum(axis=1))
# 按列除按行
print(ptResult.div(ptResult.sum(axis=1), axis=0))
# 按行除按列
print(ptResult.sum(axis=1))
print(ptResult.div(ptResult.sum(axis=0), axis=1))
