import numpy as np

a = np.array([[2, 3, 2],
              [2, 3, 2],
              [4, 2, 3]])

print(np.unique(a, axis=0))
print("--------------------")

b = np.array([[2, 3, 2],
              [2, 3, 2],
              [3, 2, 3]])
print(np.unique(b, axis=1))