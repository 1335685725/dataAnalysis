import pandas
data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.13\data.csv", sep="|")
data["total"] = data.price * data.num
print(data)

# 注意 下面的形式不行
# data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.13\data.csv", sep="|")
# data.total = data.price * data.num
# print(data)
