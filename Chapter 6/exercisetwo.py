# Exercise 2: Numpy Array ☑️

# For the array a = [20,23,82,40,32,15,67,52] 
a = [20,23,82,40,32,15,67,52]

# Print the output of following

# Find the indices of even numbers
even_indices = [i for i, x in enumerate(a) if x % 2 == 0]
print(even_indices)  # Output: [0, 3, 4, 6]

# Sort the array
a.sort()
print(a)  # Output: [15, 20, 23, 32, 40, 52, 67, 82]

# Slice elements from index 3 to the end of the array
slice1 = a[3:]
print(slice1)  # Output: [32, 40, 52, 67, 82]

# Slice elements from index 0 to index 4
slice2 = a[:5]
print(slice2)  # Output: [15, 20, 23, 32, 40]

# Print [32, 15, 67] using negative slicing
slice3 = a[-6:-3]
print(slice3)  # Output: [32, 15, 67]
