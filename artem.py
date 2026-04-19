import csv
import json
import matplotlib
import pandas as pd
import numpy as np


df = pd.read_csv('random_walk.csv')

df['distance'] = df.apply(lambda row: (row['x']**2 + row['y']**2)**0.5, axis=1)
max_distance = df['distance'].max()
mean_distance = df['distance'].mean()
print(max_distance)
print(mean_distance)
