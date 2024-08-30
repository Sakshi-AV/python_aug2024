import numpy as np

arr1 = np.arange(12)

arr2 = arr1.reshape(2,6)
arr3 = arr1.reshape(6,2)
arr4 = arr1.reshape(3,4)
arr5 = arr1.reshape(12,1)

print("Array 1= \n",arr1)
print("Array 2= \n ",arr2)
print("Array 3= \n",arr3)
print("Array 4= \n",arr4)
print("Array 5= \n",arr5)
