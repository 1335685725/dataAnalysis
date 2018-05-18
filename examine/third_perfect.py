
import pandas
from pandas import read_excel


student_data = read_excel("C:\Python\dataAnalysis\examine\students.xlsx", sheet_name="Sheet1", index_col=False)
score_data = read_excel("C:\Python\dataAnalysis\examine\score.xlsx", sheet_name="Sheet1", index_col=False)
course_data = read_excel("C:\Python\dataAnalysis\examine\course.xlsx", sheet_name="Sheet1", index_col=False)
# 将学分合并
score_data = score_data.merge(pandas.DataFrame(course_data["学分"]),
                                    left_on=score_data["课程编号"], right_on=course_data["课程编号"])
score_data = score_data.rename(columns={"学分_x": "学分"})
score_data = score_data.drop("学分_y", axis=1)
# print(score_data)
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
student_data["年级"] = student_data["班级"].str.slice(0, 3)
student_data["班级"] = student_data["班级"].str.slice(-2, )
score_data = score_data.merge(student_data.loc[:,["班级","年级","性别"]],
                              left_on=score_data["姓名"],right_on=student_data["姓名"])

gpa_grade = score_data.GPA.groupby(by=score_data["年级"]).mean()
print(gpa_grade)
if gpa_grade["一年级"] < gpa_grade["二年级"] < gpa_grade["三年级"] < gpa_grade["四年级"] :
    print("学生成绩越来越差\n, 即：\"你们是我带过的最差的一届学生观点\"成立")
else:
    print("\"你们是我带过的最差的一届学生\"\t观点不成立")