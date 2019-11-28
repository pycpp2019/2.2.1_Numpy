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
    if len(complex_array) == 0:
        return (np.array([]),np.array([]))
    data = [[abs(i), i] for i in complex_array]
    data.sort(key=lambda data: data[0])
    return (np.array(data)[:,1],np.flip(np.sort_complex(complex_array),axis = 0))

def t4_sort_string_len(string_array):
    if len(string_array) == 0:
        return(np.array([]))
    data = [[len(i), i] for i in string_array]
    data.sort(key=lambda data: data[0])
    return (np.array(data)[:,1])

def t5_sort_string_tuple(string_tuple):
    data = list(string_tuple)
    data.sort()
    return tuple(data)

'''a= np.array([1,2,3,1])
print(stats.moment(a,moment = 5))
print(np.mean((a - a.mean())**5))'''
a = np.array(["abc","abcdf","ac"])
#a =np.array([])
print (t4_sort_string_len(a))
'''
import sys
print(sys.argv)'''

