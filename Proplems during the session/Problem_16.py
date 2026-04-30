# Exercise 1: Create a 5x5 identity matrix, then set all corner values to 9
# Your code here:
import numpy as np

matrix = np.eye(5)

matrix[0, 0] = 9
matrix[0, 4] = 9
matrix[4, 0] = 9
matrix[4, 4] = 9

print(matrix)

print("-" * 70)
# Exercise 2: Create an array of 100 evenly spaced values from 0 to 2pi
# Then reshape it to a 10x10 matrix
# Your code here:

arr = np.linspace(0, 2 * np.pi, 100)
matrix = arr.reshape(10, 10)

print(matrix)

print("-" * 70)
# Exercise 3: Given this array, extract every other element in reverse order
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Expected output: [10, 8, 6, 4, 2]
# Your code here:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = arr[::-2]
print(result)