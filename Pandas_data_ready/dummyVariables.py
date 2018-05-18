# 虚拟变量，哑变量，离散特征编码，用来表示分类变量，非数量因素可能产生的影响
from pandas import read_csv
import pandas

data = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.18\data.csv", encoding="utf-8")

data["Education Level"].drop_duplicates()
educationLeavelDict = {
    'Post-Doc': 9,
    'Doctorate': 8,
    'Master\'s Degree': 7,
    'Bachelor\'s Degree': 6,
    'Associate\'s Degree': 5,
    'Some College': 4,
    'Trade School': 3,
    'High School': 2,
    'Grade School': 1,
}
data['Education Level Map'] = data['Education Level'].map(educationLeavelDict)
# print(data)
data['Gender'].drop_duplicates()
dummies = pandas.get_dummies(data, columns=['Gender'], prefix=['Gender'],
                             prefix_sep="_", dummy_na=False, drop_first=False)
print(dummies)