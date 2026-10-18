"""Task 1: NumPy Introduction & Arrays"""
import numpy as np

# Array with 10+ numbers
arr = np.array([12, 45, 7, 23, 56, 89, 34, 21, 67, 90, 15, 42])
print("Array:", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# One-dimensional array
arr_1d = np.array([1, 2, 3, 4, 5])
print("\n1-D array:", arr_1d)
print("Dimensions:", arr_1d.ndim, "| Shape:", arr_1d.shape)

# Two-dimensional array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\n2-D array:\n", arr_2d)
print("Dimensions:", arr_2d.ndim, "| Shape:", arr_2d.shape,
      "| Size:", arr_2d.size, "| dtype:", arr_2d.dtype)

# Bonus: other ways to create arrays
print("\nZeros:", np.zeros(4))
print("Arange(0,20,4):", np.arange(0, 20, 4))
print("Linspace(0,1,5):", np.linspace(0, 1, 5))
