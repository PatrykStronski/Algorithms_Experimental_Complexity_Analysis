import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

FILE_NAME = '../algorithm_exec_times_polynomials.csv'
ESTIMATION_POINT = 1000

df = pd.read_csv(FILE_NAME)
unit_length = df.loc[df.length == ESTIMATION_POINT].iloc[0].polynomial_eval / ESTIMATION_POINT ** 2
df['theoretical'] = unit_length * df['length']
unit_length_log = df.loc[df.length == ESTIMATION_POINT].iloc[0].polynomial_eval / (ESTIMATION_POINT * math.log(ESTIMATION_POINT, 10))
df['theoretical_log'] = unit_length_log * df['length'] * np.log10(df['length'])
unit_length_n = df.loc[df.length == ESTIMATION_POINT].iloc[0].polynomial_eval / ESTIMATION_POINT
df['theoretical_n'] = unit_length_n * df['length']
y_real = df.polynomial_eval

plt.plot(df.length, y_real, label='experimental')
plt.plot(df.length, df.theoretical, label='theoretical n^2')
plt.plot(df.length, df.theoretical_log, label='theoretical nlogn')
plt.plot(df.length, df.theoretical_n, label='theoretical n')
plt.xlabel('length')
plt.ylabel('time')
plt.legend()
plt.grid(True)
plt.title('Time Complexity for polynomial evaluation')
plt.show()

unit_length = df.loc[df.length == ESTIMATION_POINT].iloc[0].polynomial_eval_horner / ESTIMATION_POINT
df['theoretical'] = unit_length * df['length']
y_real = df.polynomial_eval_horner

plt.plot(df.length, y_real, label='experimental')
plt.plot(df.length, df.theoretical, label='theoretical n')
plt.xlabel('length')
plt.ylabel('time')
plt.legend()
plt.grid(True)
plt.title('Time Complexity for Horner estimation')
plt.show()