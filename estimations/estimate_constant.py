import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = '../algorithm_exec_times.csv'
ESTIMATION_POINT = 2000

df = pd.read_csv(FILE_NAME)
unit_length = df.iloc[ESTIMATION_POINT - 1].constant_function
df['theoretical'] = unit_length
y_real = df.constant_function

plt.plot(df.length, y_real, label='experimental')
plt.plot(df.length, df.theoretical, label='theoretical')
plt.xlabel('length')
plt.ylabel('time')
plt.legend()
plt.grid(True)
plt.title('Time Complexity for constant function')
plt.show()