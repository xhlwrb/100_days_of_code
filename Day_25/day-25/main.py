# weather_list = []
# continue_read = True
#
# with open("weather_data.csv", "r") as file:
#     weather_list = file.readlines()
#
# print(weather_list)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get column
# print(data["condition"])
# print(data.condition)
#
# # get row
# print(data[data.day == "Monday"])
#
# # get row where temp max
# print(data[data.temp == data.temp.max()])
#
# # get Monday's temp in fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp * 9/5 + 32)
#
# # create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
print(f"gray: {gray}, cinnamon: {cinnamon}, white: {black}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")