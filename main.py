from scipy import stats
import numpy as np


def t1_file_stat(filename):
    data = np.loadtxt(filename)
    return {
        "mean": np.mean(data),
        "max": np.max(data),
        "min": np.min(data),
        "std_dev": np.std(data),
        "5th_central_moment": stats.moment(data,moment = 5),
    }

def t2_sort_int(array):
    return (np.sort(array))

def t3_sort_complex(complex_array):
    data = {abs(i) : i for i in complex_array}
    list_keys = list(data.keys())
    list_keys.sort()
    return (np.array([data[i] for i in list_keys]),np.sort_complex(complex_array))

def t4_sort_string_len(string_array):
    data = {len(i) : i for i in string_array}
    list_keys = list(data.keys())
    list_keys.sort()
    return (np.array([data[i] for i in list_keys]))

def t5_sort_string(string_tuple):
    data = list(string_tuple)
    data.sort()
    return (data)

'''a= np.array([1,2,3,1])
print(stats.moment(a,moment = 5))
print(np.mean((a - a.mean())**5))'''


