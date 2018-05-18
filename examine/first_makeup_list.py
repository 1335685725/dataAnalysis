# 补考名单
from pandas import read_excel

student_data = read_excel("C:\Python\dataAnalysis\examine\students.xlsx", sheet_name="Sheet1", index_col=False)
score_data = read_excel("C:\Python\dataAnalysis\examine\score.xlsx", sheet_name="Sheet1", index_col=False)
# course_data = read_excel("C:\Python\dataAnalysis\examine\course.xlsx", sheet_name="Sheet1", index_col=False)
# print(course_data)
# print(score_data)
# print(student_data)

# 每门课的总成绩
score_data["最终成绩"] = score_data["平时成绩"]*0.3 + score_data["卷面成绩"] * 0.7
# 每门课的绩点
# score_data["绩点"] = round(score_data["总成绩"]/10 - 5)
# print(score_data['绩点'])
# 班级和年级
student_data["年级"] = student_data["班级"].str.slice(0, 3)
student_data["班级"] = student_data["班级"].str.slice(-2, )
# print(student_data)
score_data = score_data.merge(student_data.loc[:,["班级","年级","性别"]], left_on=score_data["姓名"],right_on=student_data["姓名"])
# print(score_data)
# 补考名单
makeup_list = score_data[score_data.最终成绩 < 60]
makeup_list = makeup_list.sort_values(by="姓名")
# print(makeup_list)
# 保存至excel
makeup_list.to_excel(excel_writer="failed.xlsx", sheet_name="makeup_list", index=False,
                     columns=["学号", "姓名","年级", "班级","性别", "课程", "课程编号","平时成绩","卷面成绩","最终成绩"])

