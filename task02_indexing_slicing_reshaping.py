"""Task 2: NumPy Indexing, Slicing & Reshaping"""
import numpy as np

arr = np.arange(10, 130, 10)          # 12 elements: 10, 20, ... 120
print("Original 1-D array:", arr)

# Indexing
print("\n--- Indexing ---")
print("First element arr[0]:", arr[0])
print("Fifth element arr[4]:", arr[4])
print("Last element arr[-1]:", arr[-1])

# Slicing
print("\n--- Slicing ---")
print("arr[2:7]  :", arr[2:7])
print("arr[:4]   :", arr[:4])
print("arr[::2]  :", arr[::2])
print("arr[::-1] :", arr[::-1])

# 2-D array
arr_2d = np.array([[11, 12, 13, 14],
                   [21, 22, 23, 24],
                   [31, 32, 33, 34]])
print("\n2-D array:\n", arr_2d)

# Rows and columns
print("\n--- Rows & Columns ---")
print("Row 1 (index 1):", arr_2d[1])
print("Column 2 (index 2):", arr_2d[:, 2])
print("Element [2][3]:", arr_2d[2, 3])
print("Sub-matrix rows 0-1, cols 1-2:\n", arr_2d[0:2, 1:3])

# Reshaping
print("\n--- Reshaping ---")
print("Original shape:", arr.shape)
print("Original array:", arr)
r1 = arr.reshape(3, 4)
print("\nReshaped to (3, 4):\n", r1)
r2 = arr.reshape(4, 3)
print("\nReshaped to (4, 3):\n", r2)
r3 = arr.reshape(2, 2, 3)
print("\nReshaped to (2, 2, 3):\n", r3)
print("\nFlattened back:", r1.flatten())
