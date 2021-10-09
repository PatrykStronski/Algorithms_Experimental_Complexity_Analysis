import csv
import statistics
import time
import random
import index1_lib
import sys

REPETITIONS = 5
CSV_EXPORT_FILE = './algorithm_exec_times_polynomials.csv'

time_list = []

for vec_len in range(1,2001):
    vec = random.sample(range(0,2000), vec_len)

    vec_times = { 'length': vec_len  }
    
    vals = []
    for i in range(0, REPETITIONS):
        time_strt = time.time()
        index1_lib.polynomialEvaluation(vec)
        time_end = time.time()
        vals.append((time_end - time_strt) * 1000)
    vec_times['polynomial_eval'] = statistics.mean(vals)
    
    vals = []
    for i in range(0, REPETITIONS):
        time_strt = time.time()
        index1_lib.polynomialEvaluationHorner(vec)
        time_end = time.time()
        vals.append((time_end - time_strt) * 1000)
    vec_times['polynomial_eval_horner'] = statistics.mean(vals)

    time_list.append(vec_times)

try:
    with open(CSV_EXPORT_FILE, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=vec_times.keys())
        writer.writeheader()
        for time_rec in time_list:
            writer.writerow(time_rec)
except IOError:
    print("I/O error")
