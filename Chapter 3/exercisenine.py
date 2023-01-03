# Optional Exercise 9: Power recursive function
# Write a program to find power of number using recursive function 
# Output: Enter the number: 2 Enter the power value: 3 The value of 2 to the power of 3 is 8

def powpow(x,y):
    if(y == 1):
        return(base) #if exponent is 1, rather than doing the process, send back base since it is the same. Helps with incompatibility of * operand for functions.
    if(y!=1):
        return(x*powpow(x,y-1)) #recursion occurs ; y-1 stops the terminal from repeating
base=int(input("\nEnter base value to be raised to the power of: "))
exp=int(input("..raised to the power of: "))
print(f"The value of {base} to the power of {exp} is:",powpow(base,exp))