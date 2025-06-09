# import csv
import pandas as pd

# with open("day25/weather_data.csv") as file_data:
#     data=csv.reader(file_data)
#     temps=[]
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))

data = pd.read_csv("day25/weather_data.csv")
print(data["temp"])