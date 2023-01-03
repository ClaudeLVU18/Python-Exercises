# Exercise 6: Exercise – Factorial☑️
# Find factorial of n numbers using recursive function 

def fac(n):  
   if n == 1:  
       return n  
   else:  #factorial formula
       return n*fac(n-1) #recursive is defined as the function calling itself from within the function itself 
  
num = int(input("Enter a number: "))  
if num < 0:  
   print("Negative numbers do not have factorials.") #error handling
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",fac(num))  