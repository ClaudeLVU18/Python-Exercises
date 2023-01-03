# Exercise 1: Input List ☑️
# Write a program that requests five numbers from the user and adds these into a list. Once the values have been inputted, displaying them to the user is a nicely formatted list.    

lst = [] # declares an empty list

for i in range(1,6): #sets the range of 1 - 5
    num = int(input(f"Enter five numbers to be added to a list. Input number {i}:")) #variable to contain the user's input of integers
    lst.append(num) #append function is used to add the user's input into the list

print("Here are the values you have listed: \n",lst)