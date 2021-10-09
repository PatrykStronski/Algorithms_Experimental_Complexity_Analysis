import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = '../algorithm_exec_times_matrix.csv'

df = pd.read_csv(FILE_NAME)
unit_length = df.iloc[0].matrix_mult
df['theoretical'] = unit_length * df['length'] ** 3
y_real = df.matrix_mult

plt.plot(df.length, y_real)
plt.plot(df.length, df.theoretical)
plt.xlabel('length')
plt.ylabel('time_matrix_mult')
plt.show()