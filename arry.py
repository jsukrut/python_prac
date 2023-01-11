import random


# Creating an array with 100 random values
array = []
print(array)
def random_array(array):
    for i in range(100):
        array.append(i)
    return array

random_array(array)
print(array)


array1 = [i  for i in range(1,101)]
print(array1)