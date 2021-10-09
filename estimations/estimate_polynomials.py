import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = '../algorithm_exec_times_polynomials.csv'

df = pd.read_csv(FILE_NAME)
unit_length = df.iloc[0].polynomial_eval
df['theoretical'] = unit_length * df['length']
y_real = df.polynomial_eval

plt.plot(df.length, y_real)
plt.plot(df.length, df.theoretical)
plt.xlabel('length')
plt.ylabel('time_polynomial_eval')
plt.show()

unit_length = df.iloc[0].polynomial_eval_horner
df['theoretical'] = unit_length * df['length']
y_real = df.polynomial_eval_horner

plt.plot(df.length, y_real)
plt.plot(df.length, df.theoretical)
plt.xlabel('length')
plt.ylabel('time_polynomial_eval_horner')
plt.show()