# Exercise 5: Product of list items☑️
# Write a program that passes a list as an argument to a function. 
# The function should then calculate the product (values multiplied) 
# of the list values and return this value back to the main program.

def prog(a):
    prod = 1
    for x in a: #takes each value in the list
        prod = prod * x 
#prod = 1 allows the variable to obtain the value of the current list element, 
#therefore multiplying them with one another as the for loop shuffles through each element
    return prod
    
             

lst = [4,5,2,8]

print(prog(lst)) #passing the list as an argument to the function