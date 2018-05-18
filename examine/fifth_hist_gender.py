'''5、你的发小小明同学由于得罪了高中班主任王老师，现在还在高中单着，
听说你拿到了学校 所有学生的名单，小明想让你计算一下你们学校的男女比例大概是怎么样子的，
各个年级的 男女比例又是怎样的。当然还是给个统计图比较容易看啦。 '''

import numpy
import matplotlib.pyplot as plt
from pandas import read_excel
import matplotlib
import pandas

student_data = read_excel("C:\Python\dataAnalysis\examine\students.xlsx", sheet_name="Sheet1", index_col=False)
student_data["年级"] = student_data["班级"].str.slice(0, 3)
student_data["班级"] = student_data["班级"].str.slice(-2, )
student_data["1"] = 1
# 设置长宽分辨率
plt.figure(figsize=(30,30), dpi=80)
font = {"family": "SimHei", "size": 80}
matplotlib.rc('font', **font)
# 绘制全校学生男女比例
result = student_data.性别.groupby(by=student_data["性别"]).count()
result = pandas.DataFrame(result)
result = result.rename(columns={"性别":"性别总人数"})
# 绘制
plt.title("全校学生男女比例")
plt.pie(result.values,
        labels=result.index,
        autopct="%.2f%%",
)
plt.savefig("全校学生男女比例.jpg")
plt.show()
# 绘制各年级学生男女比例
fig = plt.figure(figsize=(120,120), dpi=80)
font = {"family": "SimHei", "size": 240}
matplotlib.rc('font', **font)
result_pivot = student_data.pivot_table(
    values="1",
    columns="性别",
    index="年级",
    aggfunc=numpy.sum
)
# print(result_pivot)
# print(result_pivot.loc["一年级"].values)

plt.subplot(221)
plt.title("一年级学生男女比例")
plt.pie(
    result_pivot.loc["一年级"],
    labels=result_pivot.columns,
    autopct="%.2f%%",
)
plt.subplot(222)
plt.title("二年级学生男女比例")
plt.pie(
    result_pivot.loc["二年级"],
    labels=result_pivot.columns,
    autopct="%.2f%%",
)
plt.subplot(223)
plt.title("三年级学生男女比例")
plt.pie(
    result_pivot.loc["三年级"],
    labels=result_pivot.columns,
    autopct="%.2f%%",
)
plt.subplot(224)
plt.title("四年级学生男女比例")
plt.pie(
    result_pivot.loc["四年级"],
    labels=result_pivot.columns,
    autopct="%.2f%%",
)
# 其实产生这个现象的原因很简单：在 plt.show() 后调用了 plt.savefig() ，
# 在 plt.show() 后实际上已经创建了一个新的空白的图片（坐标轴），
# 这时候你再 plt.savefig() 就会保存这个新生成的空白图片。
# 在 plt.show() 之前调用 plt.savefig()；
# 画图的时候获取当前图像（这一点非常类似于 Matlab 的句柄的概念）：
# gcf: Get Current Figure
# fig = plt.gcf()
# plt.show()
# fig1.savefig('tessstttyyy.png', dpi=100)
plt.savefig("各年级学生男女比例.jpg")
plt.show()
