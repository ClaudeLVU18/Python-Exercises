# Exercise 2: Count ☑️
# The file sentences.txt has a list of string data. 
# Create a program that finds out how many times the following sentence appears 
# “Hello my name is Amster Sani”

# f = open("sentences.txt", "r")

# count = 0
# # reads each line and searches for the sentence
# string = "Hello my name is Amster Sani" 
# for string in f:
#     count += 1
  
# print(f"'{string}'\nThis sentence appears a total of: " + str(count),"times.")
# f.close()

filename = 'sentences.txt'
pi_string=''
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    pi_string += lines.strip()

number = "Hello my name is Amster Sani"
count= 0
for number in pi_string:
    count + 1

print(count)

