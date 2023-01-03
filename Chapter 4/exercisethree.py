# Exercise 3: Reading to a List ☑️
# The file numbers.txt has a list of 100 integer numbers each on a newline. 
# Create a program that puts this data into a list, then output the values in integer format.


with open('numbers.txt', 'r') as f: #file handler to open and 'r' to read file
    lst = [line.strip() for line in f]  #list is declared with containing a for loop to automatically append

for i in lst:
    print(i)


f.close()
