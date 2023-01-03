# Exercise 6 : Password Check ☑️
# Write a program to check the validity of a password given by user. The password should satisfy the following criteria:

# Contain at least 1 letter between a and z
# Contain at least 1 number between 0 and 9
# Contain at least 1 letter between A and Z
# Contain at least 1 character from $, #, @
# Minimum length of password: 6
# Maximum length of password: 12
# Ask user to include a maximum of 5 passcode attempts. Each time the user enters an incorrect passcode, they should be prompted of how many passcode attempts remain. If there are 5 failed passcode attempts the while loop should break and inform the user that the authorities have been alerted!

import re

# declaring the password criteria
password_criteria = r'^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[$#@])[a-zA-Z0-9$#@]{6,12}$'

# ask the user for their password
password = input("Enter your password: ")

# check if the password meets the criteria
if re.match(password_criteria, password):
    print("Valid password")
else:
    print("Invalid password")
