import numpy as np


from scipy import stats

def t1_file_stat(filename):
    import numpy as np 
    
    data = np.loadtxt(filename, delimiter='\t', dtype=np.float)
    dic = {}
    dic["mean"] = data.mean()
    dic["max"] = data.max()
    dic["min"] = data.min()
    dic["std_dev"] = data.std()
    dic["5th_central_moment"] = stats.moment(data,moment=5)
    return {
        "mean": dic.get("mean"),
        "max": dic.get("max"),
        "min": dic.get("min"),
        "std_dev": dic.get("std_dev"),
        "5th_central_moment": dic.get("5th_central_moment")
    }


def t2_sort_int(array):
    return  np.sort(array)
    

    
def t3_sort_complex(complex_array):
    if len(complex_array) == 0:
        return (np.array([]),np.array([]))
    tup=np.sort_complex(complex_array)
    
    module_array = np.array([abs(i) for i in complex_array])
    x = module_array.argsort()
    return (complex_array[x], np.flip(tup,axis=0))


def t4_sort_string_len(string_array):
    return np.array(sorted(string_array.tolist(), key = len))


def t5_sort_string_tuple(string_tuple):
    d=np.array(string_tuple)
    return tuple(np.sort(d))

