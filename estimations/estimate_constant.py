import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = '../algorithm_exec_times.csv'

df = pd.read_csv(FILE_NAME)
unit_length = df.iloc[0].constant_function
df['theoretical'] = unit_length
y_real = df.constant_function

plt.plot(df.length, y_real)
plt.plot(df.length, df.theoretical)
plt.xlabel('length')
plt.ylabel('time_constant')
plt.show()