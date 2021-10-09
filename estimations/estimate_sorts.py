import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

FILE_NAME = '../algorithm_exec_times.csv'
ESTIMATION_POINT = 2000

df = pd.read_csv(FILE_NAME)
unit_length = df.loc[df.length == ESTIMATION_POINT].iloc[0].bubble_sort / ESTIMATION_POINT ** 2
df['theoretical'] = unit_length * df['length'] ** 2
y_real = df.bubble_sort

plt.plot(df.length, y_real, label='real')
plt.plot(df.length, df.theoretical, label='theoretical n^2')
plt.xlabel('length')
plt.ylabel('time')
plt.legend()
plt.grid(True)
plt.title('Time Complexity for bubblesort')
plt.show()

unit_length = df.loc[df.length == ESTIMATION_POINT].iloc[0].quicksort / (ESTIMATION_POINT * math.log(ESTIMATION_POINT, 10))
df['theoretical_f'] = unit_length * df['length'] * np.log10(df['length'])
unit_length_n2 = df.loc[df.length == ESTIMATION_POINT].iloc[0].quicksort / ESTIMATION_POINT ** 2
df['theoretical_f_n2'] = unit_length_n2 * df['length'] ** 2
y_real = df.quicksort

plt.plot(df.length, y_real, label='real')
plt.plot(df.length, df.theoretical_f, label='theoretical nlogn')
plt.plot(df.length, df.theoretical_f_n2, label='theoretical n^2')
plt.xlabel('length')
plt.ylabel('time')
plt.legend()
plt.grid(True)
plt.title('Time Complexity for quicksort')
plt.show()

unit_length = df.loc[df.length == ESTIMATION_POINT].iloc[0].timsort / (ESTIMATION_POINT * math.log(ESTIMATION_POINT, 10))
df['theoretical_f'] = unit_length * df['length'] * np.log10(df['length'])
y_real = df.timsort

plt.plot(df.length, y_real, label='real')
plt.plot(df.length, df.theoretical_f, label='theoretical nlogn')
plt.xlabel('length')
plt.ylabel('time')
plt.legend()
plt.grid(True)
plt.title('Time Complexity for timsort')
plt.show()