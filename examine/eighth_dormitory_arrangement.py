'''8、学校以往都是把同个地区出来的学生尽量安排住在同个宿舍，
一来是方便各个宿舍的学生 快速熟络，组队吃鸡比较方便，
二来是彼此敦促好好学习。请你通过数据分析印证一下这个 方案的实施效果。'''

from pandas import read_excel
import pandas

student_data = read_excel("C:\Python\dataAnalysis\examine\students.xlsx", sheet_name="Sheet1", index_col=False)
score_data = read_excel("C:\Python\dataAnalysis\examine\score.xlsx", sheet_name="Sheet1", index_col=False)
# 计算绩点
score_data["最终成绩"] = score_data["平时成绩"]*0.3 + score_data["卷面成绩"] * 0.7
score_data["绩点"] = score_data["最终成绩"]/10 - 5
score_data["绩点x学分"] = score_data["绩点"] * score_data["学分"]
sum_score = score_data.groupby(by="姓名", as_index=False)["学分"].sum()
sum_score = sum_score.rename(columns={"学分": "学生个人总学分"})
score_data = score_data.merge(pandas.DataFrame(sum_score["学生个人总学分"]),
                 right_on=sum_score["姓名"], left_on=score_data["姓名"], how="outer")
sum_gpa = score_data.groupby(by="姓名", as_index=False)["绩点x学分"].sum()
sum_gpa = sum_gpa.rename(columns={"绩点x学分": "绩点x学分总和"})
score_data = score_data.merge(pandas.DataFrame(sum_gpa["绩点x学分总和"]),
                 right_on=sum_gpa["姓名"], left_on=score_data["姓名"], how="outer")
score_data["GPA"] = round(score_data["绩点x学分总和"] / score_data["学生个人总学分"], 2)
score_data = score_data.drop_duplicates("学号")
score_data = score_data.merge(pandas.DataFrame(student_data["生源地"]),
                              left_on=score_data["姓名"],
                              right_on=student_data["姓名"], how="outer")
mapshengfen = {
}
sf = score_data["生源地"].drop_duplicates()
i = 0
for shengyuandi in sf.values:
    mapshengfen[shengyuandi] = i
    i+=1
score_data["生源地编号"] = score_data["生源地"].map(mapshengfen)
relation = score_data[["GPA","生源地编号"]].corr()
print(relation)
'''方案的实施效果： 对成绩影响不明显'''
# score_data.to_excel("111.xlsx")
