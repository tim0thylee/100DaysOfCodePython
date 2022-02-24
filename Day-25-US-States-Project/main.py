# import csv
#
# # bottom is to get rows of data. uses csv library.
# with open("./weather_data.csv", mode="r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# prints the column (series) below
print(data['temp'])
# column is a "series" data type
# entire data is a "dataFrame"
data_dict = data.to_dict()

temp_list = data["temp"].to_list()

# this will get the average.
data["temp"].mean()

#Get data from a specific row
# print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp)

#create data frame
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)

#to turn into csv
data.to_csv("new_data.csv")