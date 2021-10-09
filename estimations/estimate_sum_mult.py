import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = '../algorithm_exec_times.csv'

df = pd.read_csv(FILE_NAME)
unit_length = df.iloc[0].sum_of_elements
df['theoretical'] = unit_length * df['length']
y_real = df.sum_of_elements

plt.plot(df.length, y_real)
plt.plot(df.length, df.theoretical)
plt.xlabel('length')
plt.ylabel('time_sum')
plt.show()

unit_length = df.iloc[0].product_of_elements
df['theoretical'] = unit_length * df['length']
y_real = df.product_of_elements

plt.plot(df.length, y_real)
plt.plot(df.length, df.theoretical)
plt.xlabel('length')
plt.ylabel('time_product')
plt.show()