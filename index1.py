import csv
import time
import random
import index1_lib
from matrix import Matrix

CSV_EXPORT_FILE = './algorithm_exec_times.csv'

time_list = []

for vec_len in range(1,1000):
    vec = random.sample(range(-2000,2000), vec_len)
    m1 = Matrix(vec_len)
    m2 = Matrix(vec_len)

    vec_times = { 'length': vec_len  }
    
    time_strt = time.time()
    index1_lib.constantFunction(vec)
    time_end = time.time()
    vec_times['constant_function'] = time_end - time_strt
    
    time_strt = time.time()
    index1_lib.sumOfElems(vec)
    time_end = time.time()
    vec_times['sum_of_elements'] = time_end - time_strt
    
    time_strt = time.time()
    index1_lib.productOfElems(vec)
    time_end = time.time()
    vec_times['product_of_elements'] = time_end - time_strt
    
    time_strt = time.time()
    index1_lib.polynomialEvaluation(vec)
    time_end = time.time()
    vec_times['polynomial_eval'] = time_end - time_strt
    
    time_strt = time.time()
    index1_lib.polynomialEvaluationHorner(vec)
    time_end = time.time()
    vec_times['polynomial_eval_horner'] = time_end - time_strt
    
    time_strt = time.time()
    index1_lib.bubbleSort(vec)
    time_end = time.time()
    vec_times['bubble_sort'] = time_end - time_strt
    
    time_strt = time.time()
    index1_lib.quick_sort(vec)
    time_end = time.time()
    vec_times['quicksort'] = time_end - time_strt
    
    time_strt = time.time()
    index1_lib.tim_sort(vec)
    time_end = time.time()
    vec_times['timsort'] = time_end - time_strt

    time_strt = time.time()
    Matrix.multiply_matrices(m1, m2)
    time_end = time.time()
    vec_times['matrix_mult'] = time_end - time_strt

    time_list.append(vec_times)

try:
    with open(CSV_EXPORT_FILE, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=vec_times.keys())
        writer.writeheader()
        for time_rec in time_list:
            writer.writerow(time_rec)
except IOError:
    print("I/O error")
