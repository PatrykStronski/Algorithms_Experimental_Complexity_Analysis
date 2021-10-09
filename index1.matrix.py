import csv
import time
import random
import statistics
from matrix import Matrix

CSV_EXPORT_FILE = './algorithm_exec_times_matrix.csv'
REPETITIONS = 5

time_list = []

for vec_len in range(1,500):
    m1 = Matrix(vec_len)
    m2 = Matrix(vec_len)

    vec_times = { 'length': vec_len  }

    vals = []
    for i in range(0, REPETITIONS):
        time_strt = time.time()
        Matrix.multiply_matrices(m1, m2)
        time_end = time.time()
        vals.append((time_end - time_strt) * 1000)
    vec_times['matrix_mult'] = statistics.mean(vals)

    time_list.append(vec_times)

try:
    with open(CSV_EXPORT_FILE, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=vec_times.keys())
        writer.writeheader()
        for time_rec in time_list:
            writer.writerow(time_rec)
except IOError:
    print("I/O error")
