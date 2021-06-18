import csv
import pandas as pd
import statistics

df=pd.read_csv("medium_data.csv")
claps=df["claps"].tolist()
mean=sum(claps)/len(claps)

print(mean)
