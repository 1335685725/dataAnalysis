import pandas
import numpy


df = pandas.read_csv("sitka_weather_07-2014.csv",)
print(df)

df = pandas.read_table("2.txt", sep=",", names=["age", "name"], encoding="utf-8", engine="python")
print(df)

df = pandas.read_excel("3.xlsx", sheet_name="data")
print(df)