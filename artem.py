import csv
import json
import matplotlib
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('random_walk.csv')

df['distance'] = df.apply(lambda row: (row['x']**2 + row['y']**2)**0.5, axis=1)
max_distance = df['distance'].max()
mean_distance = df['distance'].mean()
print(max_distance)
print(mean_distance)
new_df = df[df['distance'] > mean_distance]


plt.figure(figsize=(8,4))
plt.plot(new_df['x'], new_df['y'], color='green', label = 'Coordinates of walk')
plt.scatter(new_df['x'].iloc[0],new_df['y'].iloc[0], color='red', s = 10, label = 'first point', zorder=2)
plt.scatter(new_df['x'].iloc[-1],new_df['y'].iloc[-1], color='blue', s = 10, label='last point', zorder=2)
plt.legend()
plt.title('Walk')
plt.xlabel('x coordinate')
plt.ylabel('y coordinate')
plt.grid(True)
plt.show()
new_df.to_json('filtered_walk.json', orient='records',force_ascii=False, indent=4)
