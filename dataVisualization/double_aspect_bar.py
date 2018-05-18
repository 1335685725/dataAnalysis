# 双向柱形图

import pandas
import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
#%matplotlib qt
# 设置不在交互式命令行绘图，弹出新的窗口进行绘图
data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\6.4\data.csv", encoding="utf-8")
# print(data)
font = {
    "family": "Simhei"
}
matplotlib.rc("font", **font)

result = data.groupby(by=["手机品牌"], as_index=False)["月消费（元）"].agg({"月消费": numpy.sum})
result = data.pivot_table(
    values="月消费（元）",
    index="手机品牌",
    columns="通信品牌",
    aggfunc=numpy.sum
)
print(result)
result = result.sort_values(by="神州行", ascending=False)
index = numpy.arange(len(result))

min_color = (42/256, 87/256, 141/256, 1/3)# 最后一位表示透明度s
mid_color = (42/256, 87/256, 141/256, 2/3)# 最后一位表示透明度s
max_color = (42/256, 87/256, 141/256, 3/3)# 最后一位表示透明度s
plt.bar(index, result["神州行"],color=max_color)
plt.bar(index, -result["动感地带"],color=mid_color)
plt.xticks(index, result.index)
plt.legend(["神州行", "动感地带"])
plt.show()