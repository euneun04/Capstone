import numpy as np

b = np.array([[2, 3, 2],
              [2, 3, 3],
              [3, 2, 3]])
print(np.unique(b, axis=1))