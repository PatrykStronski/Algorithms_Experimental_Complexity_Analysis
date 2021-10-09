import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = '../algorithm_exec_times_matrix.csv'
ESTIMATION_POINT = 400

df = pd.read_csv(FILE_NAME)
unit_length = df.loc[df.length == ESTIMATION_POINT].iloc[0].matrix_mult / ESTIMATION_POINT ** 3
df['theoretical'] = unit_length * df['length'] ** 3
y_real = df.matrix_mult

plt.plot(df.length, y_real, label='experimental')
plt.plot(df.length, df.theoretical, label='theoretical')
plt.xlabel('length')
plt.ylabel('time')
plt.legend()
plt.grid(True)
plt.title('Time Complexity of matrix multiplication')
plt.show()