# Exercise 4: Calculator Function☑️
# The program should display the following calculator menu:

# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Modulus
# The program will prompt the user to choose the operation choice (from 1 to 5).
# Then it asks the user to input values for the calculation. 
# The program outputs the results of the calculation. 
# The program should end by asking if the user would like to perform another calculation or not.

#functions with respective formulas
def add(a,b):
    sum = a + b
    return sum

def sub(a,b):
    dif = a - b
    return dif

def mult(a,b):
    prod = a*b
    return prod
def div(a,b):
    quo = a / b
    return quo
def mod(a,b):
    rem = a % b
    return rem

while True:
    print("\nSelect a desired mathematical operation:\n")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")

    userinp = int(input("\nSelect the number of your choice: "))

    #if statements that request for two variables and sends to respective operation function
    if userinp == 1:
        userInputA = float(input("Enter first digit to be added :"))
        userInputB = float(input("Enter second digit to be added :"))
        print(add(userInputA,userInputB))
    elif userinp == 2:
        userInputA = float(input("Enter first digit to be subtracted :"))
        userInputB = float(input("Enter second digit to be subtracted :"))
        print(sub(userInputA,userInputB))
    elif userinp == 3:
        userInputA = float(input("Enter first digit to be multiplied :"))
        userInputB = float(input("Enter second digit to be multiplied :"))
        print(mult(userInputA,userInputB))
    elif userinp == 4:
        userInputA = float(input("Enter first digit to be divided :"))
        userInputB = float(input("Enter second digit to be divided :"))
        print(div(userInputA,userInputB))
    elif userinp == 5:
        userInputA = float(input("Enter first digit to be divided :"))
        userInputB = float(input("Enter second digit to be divided :"))
        print(mod(userInputA,userInputB))
    else:
        print("ERROR: not a valid selection")

    redo = input("Do you want to perform another calculation?\nEnter 'Y' to restart or another key to end: ")
    if redo.upper() == "Y":
        continue    #Keeps the while loop continuing, looping the program
    print("\n\nThank you for using this program.")
    break

      