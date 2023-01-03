# Create an integer list and perform following operations

# Create an int list with 10 values
# Output the list using a for loop
# Output the highest and lowest value
# Sort the elements in ascending order
# Sort the elements in descending order
# Append two elements
# Print the list after appending

lst = [24,60,32,45,64,74,41,34,52,83] #declaring the list with 10 values

for i in lst: #for loop that simply just displays each element
    print(i)

print(f"\nThe highest value in the list is: {max(lst)} and the lowest value is {min(lst)}.\n") #max and min function is used to display the highest value element in the list
print(f"The elements in ascending order are ", sorted(lst)) # the sorted function is used in order to arrange the elements ascendingly and descendingly
print(f"The elements in descending order are ", sorted(lst, reverse=True))

for i in range(1,3): #sets the range of 2 digits, in this case 3 indexes are declared but only two are used, this is to display 1 when 'i' is later called by output.
    inp = int(input(f"\n\nEnter two digits to be appended. Enter Digit {i}:"))
    lst.append(inp) # appends the new elements

print(lst)
