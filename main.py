import numpy as np
from scipy.stats import moment


def t1_file_stat(filename):
    with open(filename) as file:
        array = np.array([float(char.strip()) for char in file.readlines()])

    return {
        "mean": np.mean(array),
        "max": np.max(array),
        "min": np.min(array),
        "std_dev": np.std(array),
        "5th_central_moment": moment(array, moment=5)
    }

def t2_sort_int(array):
    return np.sort(array)

def t3_sort_complex(complex_array):
    return (complex_array[np.argsort(np.abs(complex_array))],
            np.array(np.sort_complex(complex_array)[::-1]))

def t4_sort_string_len(string_array):
    return string_array[np.argsort(np.char.str_len(string_array))]

def t5_sort_string_tuple(string_tuple):
    return tuple(sorted(list(string_tuple)))

if __name__ == "__main__":
    print(t3_sort_complex([1-1j,2+1j,3-6j,4,5,6-6j,7+1j,8,9-2j]))
#"test_/test.txt"