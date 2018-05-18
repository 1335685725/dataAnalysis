'''7、学校在课程设置上把 Python从入门到精通、计算机网络 这两门课程作为 Python网络 爬虫的前置课程，
但由于学时限制，计算机网络只能跟Python网络爬虫同时进行，
试探索一 下这两门前置课程对Python网络爬虫是否存在必要前置的关系，
方便教务处调整下一学年的 教学计划。 '''

import pandas
from pandas import read_excel

score_data = read_excel("C:\Python\dataAnalysis\examine\score.xlsx", sheet_name="Sheet1", index_col=False)
score_data = score_data[(score_data["课程"]=="计算机网络") |
                        (score_data["课程"]=="Python从入门到精通") |
                        (score_data["课程"]=="Python网络爬虫")]
# print(score_data)
computer_network = score_data[score_data["课程"]=="计算机网络"]
python = score_data[score_data["课程"]=="Python从入门到精通"]
spider = score_data[score_data["课程"]=="Python网络爬虫"]

computer_network["计算机成绩"] = computer_network["平时成绩"]*0.3 + computer_network["卷面成绩"]*0.7
python["python入门成绩"] = python["平时成绩"]*0.3 + python["卷面成绩"]*0.7
spider["爬虫成绩"] = spider["平时成绩"]*0.3 + spider["卷面成绩"]*0.7

score_data = score_data.merge(pandas.DataFrame(computer_network["计算机成绩"]),
                              left_on=score_data["姓名"],
                              right_on=computer_network["姓名"],
                              how="outer")
score_data = score_data.merge(pandas.DataFrame(python["python入门成绩"]),
                              left_on=score_data["姓名"],
                              right_on=python["姓名"],
                              how="outer")
score_data = score_data.merge(pandas.DataFrame(spider["爬虫成绩"]),
                              left_on=score_data["姓名"],
                              right_on=spider["姓名"],
                              how="outer")
score_data = score_data.drop_duplicates("学号")
correlation = score_data[["爬虫成绩", "python入门成绩", "计算机成绩"]].corr()
print(correlation)
print(score_data)
jielun = '''可见有爬虫成绩的同学，全都学过python入门和计算机网络，
所以把 Python从入门到精通、计算机网络 这两门课程作为 Python网络 爬虫的前置课程有必要性'''
print(jielun)
