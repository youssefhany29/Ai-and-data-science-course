import numpy as np
import time

py_list = list(range(1_000_000))
np_array = np.array(py_list)

start = time.time()
sum(py_list)
py_time = time.time()

start = time.time()
np.sum(np_array)
np_time = time.time()

print(f"{py_time}")