import pandas as pd

data=pd.read_csv("2018squirrel.csv")
dict={}
for i in data["Primary Fur Color"]:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)