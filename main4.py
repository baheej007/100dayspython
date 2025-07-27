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
data=pd.read_csv("wedata.csv")
print(data)
# print(data["temp"])
datadict=data.to_dict()
print(datadict)
# tl=[]
# # print(datadict)
# for i in range(7):
#   tl.append(datadict["temp"][i])
# avg=round(sum(tl)/len(tl),2)
# avgm=round(data['temp'].mean(),2)
# print(f"\naverage temprature of this week : {avg}")
# print(f"\naverage temprature of this week : {avgm}\n")
# print(data["temp"].max())
# print(data.condition)
mon=data[data.day=="Monday"]
print(mon.temp)
dict={
    "name":["ali","riya","bju"],
    "age":[25,21,26]
}
df=pd.DataFrame(dict)
df.to_csv("dfdict.csv")
print(df)




