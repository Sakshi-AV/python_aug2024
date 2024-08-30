import numpy as np


arr = np.arange(1, 10).reshape(3, -1)
print(arr)

arr1 = np.array((2,5,7))              # the array is  broad casted to each row 
matrix1 = np.array([[4,6,8],[12,6,20]])
result = matrix1 + arr1
print("Result =\n",result) 