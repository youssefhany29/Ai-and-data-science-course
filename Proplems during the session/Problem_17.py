#Level 4: Reshape & Dimensions 10.
#Create:
#arr = np.arange(1, 13)
#Then:
#reshape to (3,4)
#reshape to (2,6)
#try invalid reshape and handle error
import numpy as np

arr = np.arange(1, 13)
print(arr)

reshape_1 = arr.reshape(3,4)
print(reshape_1)

reshape_2 = arr.reshape(2,6)
print(reshape_2)

try:
    invalid = arr.reshape(5, 5)
except ValueError as e:
    print("Error:", e)