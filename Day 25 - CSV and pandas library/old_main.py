# with open("weather_data.csv", "r") as data:
#     contents = data.readlines()

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         temperatures.append(int(row[1]))
# print(temperatures)
#
# print(data['temp'].max())
#
# # Get Data in Column
# print(data['condition'])
# print(data.condition)

# # Get Data in Row
# print(data[data.day == "Monday"])

# Max = data['temp'].max()
# print(data[data.temp == Max])

# monday = data[data.day == "Monday"]
# t = monday.temp
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "score": [76, 59, 94],
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")  # The path to csv file
# print(data)

import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

Gray = len(df[df["Primary Fur Color"] == "Gray"])
Black = len(df[df["Primary Fur Color"] == "Black"])
Cinnamon = len(df[df["Primary Fur Color"] == "Cinnamon"])

data = {
    "color": ["Black", "Gray", "Cinnamon"],
    "number": [Black, Gray, Cinnamon]
}
data = pd.DataFrame(data)
data.to_csv("Color_data.csv")
