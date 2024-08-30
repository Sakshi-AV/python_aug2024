import numpy as np

arr1 = np.arange(1, 10)
arr2 = np.arange(2, 25, 2)

arr3 = arr1.reshape(3, -1)
arr4 = arr2.reshape(4, -1)
arr5 = arr2.reshape(2, -1)
arr6 = arr2.reshape(3, -1)
arr7 = arr2.reshape(-1, 4) 

print('Array 1:\n', arr1)
print('Array 2:\n', arr2)
print('Array 3:\n', arr3)
print('Array 4:\n', arr4)
print('Array 5:\n', arr5)
print('Array 6:\n', arr6)
print('Array 7:\n', arr7)