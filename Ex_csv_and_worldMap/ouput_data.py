from pandas import DataFrame

df = DataFrame({
    "age": [21, 22, 23],
    "name": ["ken", "John", "JIMI"]
})
df.to_csv(r"C:\\Users\\Benlyons\\Desktop\\WorkSpace\\py\\df.csv", index=False) #不需要默认索引