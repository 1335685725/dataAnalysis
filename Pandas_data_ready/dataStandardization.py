# 数据标准化 0-1标准化, 是指将数据按比例缩放，使之落入特定区域
# x* = (x - min)/(max - min)
import pandas
data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.14\data.csv")

data["scale"] = round(
    (data.score-data.score.min())/(data.score.max()-data.score.min()), 2
)
print(data)