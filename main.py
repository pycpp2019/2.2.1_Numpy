import numpy as np


def t1_file_stat(filename):
    with open(filename, "r") as f:
        data = np.array([int(l) for l in [l.strip() for l in f] if len(l) > 0])
    mean = data.mean()
    cm5 = np.mean((data - mean)**5)
    return {
        "mean": mean,
        "max": data.max(),
        "min": data.min(),
        "std_dev": data.std(),
        "5th_central_moment": cm5,
    }

def t2_sort_int(array):
    return np.sort(array)

def t3_sort_complex(complex_array):
    abssort = complex_array[np.argsort(np.abs(complex_array))]
    rresort = np.flip(np.sort(complex_array))
    return (abssort, rresort)

def t4_sort_string_len(string_array):
    #np.random.shuffle(string_array)
    return string_array[np.argsort(np.vectorize(len)(string_array))]

def t5_sort_string_tuple(string_tuple):
    return tuple(sorted(string_tuple))
