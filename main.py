import numpy as np
from scipy.stats import moment 


def t1_file_stat(filename):
    file = open(filename, 'r')
    arr = np.array([int(line) for line in file if line], int)
    file.close()
    return {
        "mean": np.mean(arr),
        "max": np.amax(arr),
        "min": np.amin(arr),
        "std_dev": np.std(arr),
        "5th_central_moment": moment(arr, moment =5),
    }

def t2_sort_int(array):
    return np.sort(array)

def t3_sort_complex(complex_array):
    return (
        complex_array[np.argsort(np.abs(complex_array), kind ='mergesort')],
        np.sort(complex_array)[::-1])

def t4_sort_string_len(string_array):
    return string_array[np.argsort(np.array([len(el) for el in string_array]))]

def t5_sort_string_tuple(string_tuple):
    return string_tuple.sort()