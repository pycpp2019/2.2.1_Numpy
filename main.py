import numpy as np
def t1_file_stat(filename):
	values=np.genfromtxt(filename, delimiter="\n")
	ans={'mean':0,'max':0,'min':0,'std_dev':0,'5th_central_moment':0}
	ans['mean']=np.mean(values)
	ans['max']=np.max(values)
	ans['min']=np.min(values)
	m=np.mean(values)
	s=0
	for i in values:
		s+=(i-m)**2
	ans['std_dev']=(s/len(values))**(1/2)
	s=0
	u=dict.fromkeys(np.unique(values),0.0)
	for i in values:
		u[i]+=1
	for i in values:
		s+=((i-m)**5)*u[i]/len(values)
	ans['5th_central_moment']=s
	return ans
def sortByLength(inputStr):
        return len(inputStr)

def sortByNorm(inputComplex):
		return (inputComplex.real**2+inputComplex.imag**2)**(1/2)
#print(t1_file_stat("a.txt"))
def t2_sort_int(array):
	return np.sort(array)

def t3_sort_complex(complex_array):
	sortList=list(complex_array)
	newList=sorted(sortList, key=sortByNorm)
	return (np.sort(array),np.array(newList))

def t4_sort_string_len(string_array):
	sortList=list(string_array)
	newList=sorted(sortList, key=sortByLength)
	return np.array(newList)

def t5_sort_string_tuple(string_tuple):
	string_tuple1=np.array(string_tuple,dtype=string)
	return np.sort(string_tuple1)

#arr=np.array(['j','jfkkpppppp','abc'])
#print(t4_sort_string_len(arr))
