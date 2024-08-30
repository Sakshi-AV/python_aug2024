import numpy as np

array1 = np.array((2,12,3,15,25,45))
print("Array 1 =\n",array1)

roots = np.sqrt(array1)
print("Roots =\n",roots)

exponential = np.exp(array1)
print("Exponential  =\n",exponential)

print("Element at index 3 =",array1[3])

array2 = array1[1:5]
print("Sliced array = ",array2)

