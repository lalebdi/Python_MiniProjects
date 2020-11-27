# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temps = []
#     for row in data:
#         if row[1] != 'temp':
#             temps.append(int(row[1]))
#     print(temps)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average= sum(temp_list) / len(temp_list)
print(average)
print(data["temp"].mean())

print(data["temp"].max())

# Get Data in Columns
print(data["condition"])
print(data.condition)

# data in rows -> first select the column and then match the row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()]) # highest temp row
monday = data[data.day == "Monday"]
print(monday.condition)
# Mondays temp in f
temp_in_f = int(monday.temp) * 9/5 + 32
print(temp_in_f)

# Creating a new dataframe
scores_dict = {
    "students": ["Amy", "James", "Angels"],
    "scores": [76, 56, 65]
}

create = pandas.DataFrame(scores_dict)
# print(create)
create.to_csv("new_data.csv")
