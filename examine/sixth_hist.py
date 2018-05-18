#6、胶水儿老师想让你帮忙统计一下她所教的课程各个分数段的分布大概是怎样的，
# 请你用直方图帮她做一下统计

from pandas import read_excel
import matplotlib.pyplot as plt
import matplotlib

score_data = read_excel("C:\Python\dataAnalysis\examine\score.xlsx", sheet_name="Sheet1", index_col=False)
course_data = read_excel("C:\Python\dataAnalysis\examine\course.xlsx", sheet_name="Sheet1", index_col=False)

course_data = course_data[course_data["教师"]=="胶水儿"]
score_data = score_data[score_data["课程编号"] == course_data["课程编号"][6]]
score_data["总成绩"] = score_data["平时成绩"]*0.3 + score_data["卷面成绩"]*0.7
print(score_data)
font = {"family": "Simhei"}
matplotlib.rc("font", **font)
main_color = (42/256, 87/256, 141/256, 0.7)# 最后一位表示透明度s
plt.xlabel('成绩')
plt.ylabel('人数')
plt.title('胶水儿老师所教的课程各个分数段的分布')
plt.hist(score_data["总成绩"], bins=10, color=main_color, cumulative=False)
plt.grid(True)
plt.savefig("hist")
plt.show()