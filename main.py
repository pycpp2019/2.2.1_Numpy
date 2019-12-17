import numpy as np
import scipy.stats
import re
def t1_file_stat(filename):
    data_ = np.loadtxt(filename, delimiter = '\n', dtype = np.int, usecols = len(re.findall(r"[\n']+", filename))) 
    if data_.size < 2:
        return "Try again"
    else:
        return {                
        "mean": data_.mean(),
        "max": data_.max(),
        "min": data_.min(),
        "std_dev": data_.std(),
        "5th_central_moment": scipy.stats.moment(data_, moment = 5, nan_policy='propagate'),
        }
def t2_sort_int(array):
    return sorted(array)
def t3_sort_complex(complex_array):
    return (np.array(sorted(complex_array, key = abs)), np.array(sorted(complex_array, key = lambda x: x.real)[::-1]))
def t4_sort_string_len(string_array):
    return np.array(sorted(string_array, key = len))
def t5_sort_string_tuple(string_tuple):
    return tuple(sorted(string_tuple))