import numpy as np

data1 = np.array([10, 20, 30, 40, 50])
data2 = np.array([2, 4, 5, 8, 10])

print("Dataset 1:", data1)
print("Dataset 2:", data2)

print("\n--- Mathematical Operations ---")

print("Addition:", data1 + data2)

print("Subtraction:", data1 - data2)

print("Multiplication:", data1 * data2)

print("Division:", data1 / data2)

print("\n--- Statistical Functions ---")

print("Mean:", np.mean(data1))

print("Median:", np.median(data1))

print("Minimum:", np.min(data1))

print("Maximum:", np.max(data1))

print("Standard Deviation:", np.std(data1))

print("Sum:", np.sum(data1))