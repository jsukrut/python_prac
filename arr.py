import array as arr
import sys
import numpy as np

np_arr = np.array([1, 2, 3, 4, 5])
a = arr.array('i', [1, 2, 3])
l = [1,2,3]


print(sys.getsizeof(a))
print(sys.getsizeof(l))
print(sys.getsizeof(np_arr))