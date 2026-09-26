import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original Array:")
print(arr)

print("\nElement at index 0:", arr[0])
print("Element at index 4:", arr[4])
print("Element at index 7:", arr[7])

print("\nSliced Array (index 2 to 6):")
print(arr[2:7])

# Create a two-dimensional array
two_d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nTwo-Dimensional Array:")
print(two_d)

print("\nFirst Row:")
print(two_d[0])

print("\nSecond Row:")
print(two_d[1])

print("\nFirst Column:")
print(two_d[:, 0])

print("\nSecond Column:")
print(two_d[:, 1])

print("\nElement at Row 2, Column 3:")
print(two_d[1, 2])

reshaped = arr.reshape(2, 5)

print("\nOriginal Array:")
print(arr)

print("\nReshaped Array (2 x 5):")
print(reshaped)