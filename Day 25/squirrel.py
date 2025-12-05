import pandas as pd
import numpy as np

# count of squirrels on the basis of fur color

df = pd.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# fur_colors_dict = pd.DataFrame(df["Primary Fur Color"].value_counts())
# fur_colors_dict.to_csv('squirrel_count.csv')
# print(fur_colors_dict)

gray_sq = df[df["Primary Fur Color"] == "Gray"]
cinnamom_sq = df[df["Primary Fur Color"] == "Cinnamon"]
black_sq = df[df["Primary Fur Color"] == "Black"]

gray_sq_count = len(gray_sq)
cinnamom_sq_count = len(cinnamom_sq)
black_sq_count = len(black_sq)
df_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray_sq_count,cinnamom_sq_count,black_sq_count]
}
data_df = pd.DataFrame(df_dict)
data_df.to_csv("sq_count.csv")









