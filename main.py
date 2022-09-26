import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = 0
cinnamon_count = 0
black_count = 0


data_dict = (data["Primary Fur Color"].to_dict())
print(data_dict)
for color in data_dict.values():
    if color == "Gray":
        gray_count += 1
    elif color == "Cinnamon":
        cinnamon_count += 1
    elif color == "Black":
        black_count += 1

print(gray_count)
print(cinnamon_count)
print(black_count)
# data_sq.to_csv("squirrel_count.csv")

#Dataframe

sq_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "scores": [gray_count, cinnamon_count, black_count]
}
sq_data = pandas.DataFrame(sq_dict)
sq_data.to_csv("squirrel_count.csv")