import numpy as np

# Create a 1D NumPy array
array = np.array([1, 2, 4, 7, 11])

# Calculate the gradient
gradient = np.gradient(array)

print("Original array:")
print(array)

print("\nGradient array:")
print(gradient)