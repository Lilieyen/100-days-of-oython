# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas as pandas
# import pandas as pd
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# # average_temp = sum(temp_list)/len(temp_list)
# # print(round(average_temp, 2))
# print(data['temp'].mean())
# print(data['temp'].max())

# # Get Data in columns
# print(data["condition"])
# print(data.condition)
#
# # Get Data in Row
# print(data[data.day == "Monday"])

# Get Data when temp was max
# print(data[data.temp == data.temp.max()])
# print(data[data["temp"] == data["temp"].min()])

# create a dataFrame from scratch
# data_dict = {
#     "students": ["Lilian", "Nyasita", "Mokaya"],
#     "scores": [50, 70, 90]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

my_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_color = my_data["Primary Fur Color"]
# print(fur_color)
grey_squirrels = len(my_data[my_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(my_data[my_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(my_data[my_data["Primary Fur Color"] == "Black"])
print(grey_squirrels)
print(cinnamon_squirrels)
print(black_squirrels)

# create a new data frame
fur_color_count = {
    "fur_color": ["Gray", "Cinnamon", "Black"],
    "count" : [grey_squirrels, cinnamon_squirrels, black_squirrels]
}
df = pandas.DataFrame(fur_color_count)
df.to_csv("Squirrel_count.csv")
