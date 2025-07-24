import csv
# with open ("weather_data.csv","r") as f:
#     data= csv.reader(f)
#     temp=[]
#     for row in data:
#         if row[1]!="temp":
#          temp.append(int(row[1]))
#         print(row)
#     print(temp)

import pandas as pd
data=pd.read_csv("weather_data.csv")
# print(data["temp"])
datadict=data.to_dict()
print(datadict)
print(datadict["day"][0])