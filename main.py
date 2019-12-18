import numpy as np
from scipy.stats import moment

def t1_file_stat(filename):
    # your solution
    data=np.genfromtxt(filename, delimiter="\n", dtype=np.float)
    return {
        "mean": np.mean(data),
        "max": np.max(data),
        "min": np.min(data),
        "std_dev": np.std(data),
        "5th_central_moment": moment(data, 5),
    }

def t2_sort_int(array):
    return np.sort(array)

def t3_sort_complex(complex_array):
    return (complex_array[np.argsort([abs(num) for num in complex_array])], np.sort_complex(complex_array)[::-1])

def t4_sort_string_len(string_array):
    return string_array[np.argsort(np.array([len(s) for s in string_array]))]

def t5_sort_string_tuple(string_tuple):
    return tuple(np.sort(np.array(string_tuple)))
