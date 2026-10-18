"""Task 3: NumPy Mathematical & Statistical Operations"""
import numpy as np

# Dataset: monthly units sold in two stores (Jan-Dec)
store_a = np.array([120, 135, 150, 160, 145, 170, 180, 175, 190, 200, 210, 230])
store_b = np.array([100, 110, 130, 125, 140, 150, 155, 165, 160, 175, 185, 195])
print("Store A:", store_a)
print("Store B:", store_b)

print("\n=== Mathematical Operations ===")
print("Addition       (A + B):", store_a + store_b)
print("Subtraction    (A - B):", store_a - store_b)
print("Multiplication (A * B):", store_a * store_b)
print("Division       (A / B):", np.round(store_a / store_b, 2))

print("\n=== Statistical Functions (Store A) ===")
print("Mean               :", np.mean(store_a))
print("Median             :", np.median(store_a))
print("Minimum            :", np.min(store_a))
print("Maximum            :", np.max(store_a))
print("Standard Deviation :", round(np.std(store_a), 2))
print("Sum                :", np.sum(store_a))

print("\n=== Statistical Functions (Store B) ===")
print("Mean               :", np.mean(store_b))
print("Median             :", np.median(store_b))
print("Minimum            :", np.min(store_b))
print("Maximum            :", np.max(store_b))
print("Standard Deviation :", round(np.std(store_b), 2))
print("Sum                :", np.sum(store_b))

print("\nBest month for Store A (index):", np.argmax(store_a) + 1)
