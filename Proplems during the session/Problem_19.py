import numpy as np

mat = np.zeros((5,5))
mat[0, :] = 1
mat[-1, :] = 1
mat[:, 0] = 1
mat[:, -1] = 1
print(mat)

