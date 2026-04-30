#Level 5: Random & Attributes 13.
#Generate:
#3x3 uniform random array
#3x3 normal distribution
#Then print:
#shape
#ndim
#size
#dtype

import numpy as np
uni_arr = np.random.rand((3,3))

print(uni_arr.shape)
print(uni_arr.ndim)
print(uni_arr.size)
print(uni_arr.dtype)

norm_arr = np.random.randn((3,3))


print(norm_arr.shape)
print(norm_arr.ndim)
print(norm_arr.size)
print(norm_arr.dtype)