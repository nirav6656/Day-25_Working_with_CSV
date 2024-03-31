import csv
import math
import pandas
with (open("weather_data.csv") as data_file):
    data = pandas.read_csv(data_file)

    monday_temp = data[data.day == "Monday"]
    print((monday_temp.temp * 9 / 5) + 32)
    # average = sum(df)/len(df)
    # print(df.max())

