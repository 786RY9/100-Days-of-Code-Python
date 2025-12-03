import csv
import pandas as pd
import pandas

# with open('Day 25/weather_data.csv') as file:
#     data = file.readlines()

# print(data)



# with open('Day 25/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
    
#     i = 0 
#     for row in data:
#         # print(row)
#         # print(i)
#         if i>0:
#             temperatures.append(int(row[1]))
#         if i == 0:
#             i+=1

#     print(temperatures)




df = pandas.read_csv("Day 25/weather_data.csv")
# print(type(df))
# print(df)
# print(type(df['temp']))
# print(df.to_dict())

# print(df['temp'].to_list())

# total = df['temp'].sum()
# print(total/len(df['temp']))

# print(df['temp'].mean())

# print(df['temp'].max())



# print(df.condition)

# # get data of a particular row
# print(df[df['day']=='Monday'])


# print(df[df['temp']==df['temp'].max()].temp*9/5+32)

data_dict = {
    'students':['aj','jj','ali','hamza','ans','ry'],
    'marks':[98,99,96,97,96,92]
}

data = pd.DataFrame(data_dict)
data.to_csv('new_data.csv')










