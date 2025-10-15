import numpy as np

arr = np.array([11, 22, 33, 44, 55])
print(arr.dtype)

arr = arr.astype(np.float32)
print(arr.dtype)

arr2 = arr.resize(3, 2)
print(arr2)

arr3 = arr.reshape(-1, 2)
print(arr3)