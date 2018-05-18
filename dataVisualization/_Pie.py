# 主要显示各部分占比情况
# pie(x：绘图的序列,colors：饼图各部分颜色, explode：需要突出的块状的序列, autopct：饼图占比的显示格式，如%.2f)
import pandas
import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
#%matplotlib qt
# 设置不在交互式命令行绘图，弹出新的窗口进行绘图
data = pandas.read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\6.3\data.csv", encoding="utf-8")
print(data)
result = data.groupby(by=["通信品牌"], as_index=False)["号码"].agg({
    "用户数": numpy.size
})
print(result)
# 设置长宽分辨率
plt.figure(figsize=(30,30), dpi=80)
font = {"family": "SimHei", "size": 50}
# fontProp = font_manager.FontProperties(
#     fname="C:\\Windows\\Fonts\\FZSTK.TTF"
# )
# 设置字体
# font = {
#     'family': fontProp.get_name(),
#     'size': 20
# }
matplotlib.rc('font', **font)
# 设置突出部分
explode = (0.3,0,0)
# 设置横轴和纵轴等长的饼图
plt.axis("equal")
plt.pie(result["用户数"],
        labels=result["通信品牌"],
        autopct="%.2f%%",
        explode=explode,
startangle=67
)
plt.show()
