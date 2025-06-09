import pandas as pd
data = pd.read_csv("day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(f"Gray Squirrels: {gray_squirrels}")
print(f"Red Squirrels: {red_squirrels}")
print(f"Black Squirrels: {black_squirrels}")
#save to new CSV
data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}
data_frame = pd.DataFrame(data_dict)
data_frame.to_csv("day25/squirrel_count.csv", index=False)