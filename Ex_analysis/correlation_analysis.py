# 相关分析,主要采用皮尔逊相关系数r来度量连续变量之间的线性相关强度
# r=0表示不存在线性关系，不代表没有关系
# r>0时线性正相关，<0时线性负相关
# 0.1<=|r|<0.3 低度相关
# 0.3<=|r|<0.8 中度相关
# 0.8<=|r|<=1 高度相关
# 相关分析函数 DataFrame.corr()->DataFrane分析每个列两两之间的相似度,
# Series.corr(other)->数值 计算该序列和other序列之间的相关度
import pandas



data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\5.6\data.csv", encoding="utf-8")
print(data)
# 人口和文盲率的相关度
print(data["人口"].corr(data["文盲率"])
)
# 多列之间的相关度计算
# print(data[["超市购物率", "网上购物率", "文盲率", "人口"]]
# )
a = data[["超市购物率", "网上购物率", "文盲率", "人口"]].corr()
print(a)