from pandas import read_csv
import pandas
import datetime

# data = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.17\data.csv", encoding="utf-8")
#
# print(data)
dataparse = lambda dates: pandas.datetime.strptime(dates, "%Y%m%d")


# data = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.17\data.csv",
#                 encoding="utf-8",
#                 parse_dates=["date"],
#                 date_parser=dataparse,
#                 index_col='date'
# )
# print(data)

dt1 = datetime.date(year=2016, month=2, day=1)
dt2 = datetime.date(year=2016, month=2, day=5)

# print(data.ix[dt1: dt2])
# print(data.ix[[dt1, dt2]])
data = read_csv(r"C:\Users\Benlyons\Desktop\WorkSpace\py\dateanasisy\4.17\data.csv",
                encoding="utf-8",
                parse_dates=["date"],
                date_parser=lambda dates: pandas.datetime.strptime(dates, "%Y%m%d"),
)
data[(data.date >= dt1) & (data.date <= dt2)]
print(data[(data.date >= dt1) & (data.date <= dt2)]
)