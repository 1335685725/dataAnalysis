# 柱形图：是一种以长方形的单位长度，根据数据大小绘制的统计图，用来比较两个或者以上的数据（时间或者类别）
#bar(left:x轴位置序列, height:y轴的数值序列, width:柱形图库宽度, color:柱形图填充颜色)
#barh(bottom, width, height, color)

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
# print(result)
# 配置颜色
main_color = (42/256, 87/256, 141/256, 1)# 最后一位表示透明度s
# 排序
sgb = result.sort_values(by="月消费",ascending=False)
print(sgb)
# 竖向柱形图
index = numpy.arange(sgb.月消费.size)
print(index)
# plt.bar(index, sgb["月消费"], color=main_color)
# plt.xticks(index, sgb.手机品牌)
# 横向柱形图
# plt.barh(index, sgb["月消费"], color=main_color)
# plt.yticks(index, sgb.手机品牌)
# plt.show()

#  多组数据进行绘制柱形图
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

plt.bar(index, result["神州行"],color=max_color,width=1/4)
plt.bar(index+1/4, result["动感地带"],color=mid_color,width=1/4)
plt.bar(index+2/4, result["全球通"],color=min_color,width=1/4)

plt.xticks(index+1/3, result.index)
plt.legend(["神州行", "动感地带", "全球通"])
plt.show()