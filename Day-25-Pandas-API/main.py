# # import csv
# #
# # # bottom is to get rows of data. uses csv library.
# # with open("./weather_data.csv", mode="r") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # prints the column (series) below
# print(data['temp'])
# # column is a "series" data type
# # entire data is a "dataFrame"
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
#
# # this will get the average.
# data["temp"].mean()
#
# #Get data from a specific row
# # print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
#
# #create data frame
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
#
# #to turn into csv
# data.to_csv("new_data.csv")

# how many gray, cinnamon, and black squierrels in a csv file/

import pandas

#read the csv file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#count each color
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"].count().X
#can also do len(data[data["Primary Fur Color"] == "Cinnamon"]) since it's treated like a list. 
gray = data[data["Primary Fur Color"] == "Gray"].count().X
black = data[data["Primary Fur Color"] == "Black"].count().X
#create the dictionary
data_dict = {
    "Fur Color": ["Cinnamon", "Gray", "Black"],
    "Count": [cinnamon, gray, black]
}
#export to csv
data = pandas.DataFrame(data_dict)
data.to_csv("color_count.csv")