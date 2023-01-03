# Exercise 1: Format Name☑️
# Write a function that takes a first and last name through user input, and returns a neatly formatted full name.    

def userName(x): # x gets the value passed when the function is called
    surName = input("Now, enter your surname: ") #simple input command
    return(f"Good day, {x} {surName}.")
 
name = input("Please enter your first name: ")

print(userName(name)) #name is passed onto 'x' in the function