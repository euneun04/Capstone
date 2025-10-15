import numpy as np

a = np.array([[2, 3, 4],
              [5, 4, 7],
              [4, 2, 3]])

print(np.unique(a))

print(np.unique(a, return_index=True))
v, c = np.unique(a, return_index=True)
print(v)
print(c)
print("--------------------")

print(np.unique(a, return_counts=True))
print(np.unique(a, return_inverse=True))