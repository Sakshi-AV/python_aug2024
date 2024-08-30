import numpy as np

vector = np.arange(5)
print('Vector:\n', vector)
print("Vector shape:\n", vector.shape)

matrix = np.ones([3, 2])
print("Matrix:\n", matrix)
print("Matrix shape:", matrix.shape)

tensor = np.zeros([2, 3, 3])
print("Tensor:\n", tensor)
print("Tensor shape:\n", tensor.shape)

print(tensor[0][1][1])