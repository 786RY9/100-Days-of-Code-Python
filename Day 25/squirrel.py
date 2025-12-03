import pandas as pd
import numpy as np

# count of squirrels on the basis of fur color

df = pd.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colors_dict = pd.DataFrame(df["Primary Fur Color"].value_counts())
fur_colors_dict.to_csv('squirrel_count.csv')
# print(fur_colors_dict)













