# Exercise 1: User information ☑️
# Write a program to create a file called bio.txt
# and write the following information to the file 
# asking user to enter the values: Name Age Hometown 
# Each piece of data should be on a new line 
# Once the data has been written to the file, read the data from the file and output the data. 

file = 'bio.txt' #declaring file name

userName = input("Enter your full name: ")
userAge = input("Enter your age: ") #input
userHome = input("Enter your hometown: ")

with open(file, 'w') as file_handler: #writes to file
    file_handler.write(f"{userName}\n{userAge}\n{userHome}") #placing variables in string format in order to make use of\n next line function
