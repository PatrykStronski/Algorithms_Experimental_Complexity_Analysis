import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = '../algorithm_exec_times.csv'
ESTIMATION_POINT = 2000

df = pd.read_csv(FILE_NAME)
unit_length = df.loc[df.length == ESTIMATION_POINT].iloc[0].sum_of_elements / ESTIMATION_POINT
df['theoretical'] = unit_length * df['length']
y_real = df.sum_of_elements

plt.plot(df.length, y_real, label='experimental')
plt.plot(df.length, df.theoretical, label='theoretical')
plt.xlabel('length')
plt.ylabel('time')
plt.legend()
plt.grid(True)
plt.title('Time Complexity sum of elems')
plt.show()

unit_length = df.loc[df.length == ESTIMATION_POINT].iloc[0].product_of_elements / ESTIMATION_POINT
df['theoretical'] = unit_length * df['length']
y_real = df.product_of_elements

plt.plot(df.length, y_real, label='experimental')
plt.plot(df.length, df.theoretical, label='theoretical')
plt.xlabel('length')
plt.ylabel('time')
plt.legend()
plt.grid(True)
plt.title('Time Complexity product of elems')
plt.show()