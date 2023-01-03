# Exercise 4: Year Tuples☑️

# Create a tuple with values
year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

# Access the value at index -3
print("Value at index [-3] is ",year[-3])

# Reverse the tuple and print the original tuple and reversed tuple
yearnew= year[::-1]
print("Original Tuple: ",year)
print("Reversed Tuple: ",yearnew)

# Count number of times 2009 is in the tuple (use count() method)
print("2009 appears a total of",year.count(2009),"times")

# Get the index value of 2018(Use index method)
print("The index value of '2018' is: ",year.index(2018))

# Find length of given tuple(Use len() method)
print("The length of the tuple is: ",len(year))





