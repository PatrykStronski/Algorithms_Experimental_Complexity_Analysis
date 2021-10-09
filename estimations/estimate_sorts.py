import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = '../algorithm_exec_times.csv'

df = pd.read_csv(FILE_NAME)
unit_length = df.iloc[0].bubble_sort
df['theoretical'] = unit_length * df['length'] ** 2
y_real = df.bubble_sort

plt.plot(df.length, y_real)
plt.plot(df.length, df.theoretical)
plt.xlabel('length')
plt.ylabel('time_bubble_sort')
plt.show()

unit_length = df.iloc[0].quicksort
df['theoretical_f'] = unit_length * df['length'] * np.log10(df['length'])
y_real = df.quicksort

plt.plot(df.length, y_real)
plt.plot(df.length, df.theoretical_f)
plt.xlabel('length')
plt.ylabel('time_quick_sort')
plt.show()

unit_length = df.iloc[0].timsort
df['theoretical_f'] = unit_length * df['length'] * np.log10(df['length'])
y_real = df.timsort

plt.plot(df.length, y_real)
plt.plot(df.length, df.theoretical_f)
plt.xlabel('length')
plt.ylabel('time_tim_sort')
plt.show()