import operator

# the main menu is displayed with the use of a while loop in order to allow user to repeat the calculations unless 'Q' is entered.
while True:
    print("\n\nCalculator menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")
    choice = input("Enter the operation choice (1-6) or Q to quit: ")

    # checks whether the user inputs the letter "Q", may it be in lower case or upper case. 
    # Since we are only in need of one letter, only two characters are needed to be found. 
    if choice == "Q" or "q":
        break
    #checks if the user input is anything other than "Q". Used for error handling.
    elif not choice.isdigit() or int(choice) not in range(1, 7): 
        print("Invalid choice. Please try again.")
        continue

    # First, we take user input in the form of string in order to create a program that allows for error handling in the case
    # of a string being entered instead of a number.
    value1_str = input("Enter the first value: ")
    value2_str = input("Enter the second value: ")

    # Reads the string to see if user input is a valid number.
    # we use .isdigit() in order to check whether the value is a number or not
    if not value1_str.isdigit():
        print("Error: Invalid input. Please enter a number for the first value.")
        continue
    if not value2_str.isdigit():
        print("Error: Invalid input. Please enter a number for the second value.")
        continue

    # once values are confirmed to be numbers, they are converted to float values
    a = float(value1_str)
    b = float(value2_str)
    if choice == "4" and b == 0:
        print("Error: Cannot divide by zero.")
    else: #making use of the operator module from the operator library
        if choice == "1":
            print(operator.add(a, b))
        elif choice == "2":
            print(operator.sub(a, b))
        elif choice == "3":
            print(operator.mul(a, b))
        elif choice == "4":
            print(operator.truediv(a, b))
        elif choice == "5":
            print(operator.mod(a, b))
        elif choice == "6":
            print(operator.gt(a, b))
