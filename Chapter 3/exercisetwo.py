# Exercise 2: Sum Function☑️
# Write a program that calculates the sum of two values. The program should get the two values from user input and output the results to screen.    

def sumUp(x,y): #function that takes two values in x and y 
    return x + y

a = int(input("Enter two digits to be summed up. Digit 1: "))
b = int(input("Enter two digits to be summed up. Digit 2: "))

print("\n\nSum: ",sumUp(a,b)) #sends over the user in put values in the form of a and b into the function's parameters of x and y

