# 随机抽样
# 随机抽样函数 DataFrame.sample(n, frac, replace=False) -> DataFrame
# 参数说明 n按个数抽样，frac按百分比抽样，replace 是否放回抽样，默认False不放回
import numpy, pandas

data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.9\data.csv")

# 设置随机种子
# numpy.random.seed(5)

# 按照个数抽样
data = data.sample(n = 10)
# print(data)
# 按百分比抽样
data = data.sample(frac=0.02)
# print(data)
# replace = True可放回抽样
# replace = False不可放回抽样
data = data.sample(n=10, replace=True)
# print(data)

# 典型抽样
gbr = data.groupby("class") # 获得分组之后的对象，对class列进行分组
gbr = gbr.groups # 获取分组后的字典
# 看看gbr里面有什么
# for k, v in gbr.items():
#     print(k , "-------" , v)
# key是分组名，value是在这个分组取多少个样本
typicalNDict = {
    1:2,
    2:4,
    3:6
}

def typicalSampling(group, typicalN_Dict):
    name = group.name
    n = typicalN_Dict[name]
    return group.sample(n=n)

result = data.groupby("class", group_keys=True).apply(typicalSampling, typicalNDict)
print(result)

def typicalFracSampling(group, typicalFracDict):
    name = group.name
    frac = typicalFracDict[name]
    return group.sample(frac=frac)

typicalFracDict = {
    1:0.2,
    2:0.4,
    3:0.6
}

result = data.groupby("class", group_keys=False).apply(typicalFracSampling, typicalFracDict)
print(result)

