# Optional Exercise 8: Count characters
# Write program to count number of vowels and consonants in the given string Output:

# Enter a word: hello world

userInput = input("Enter a word: ")
print("Total number of letters: ",len(userInput))
# Total number of letters: 11
# Number of vowels:  3

# using for-each loop, character is reference to a letter in the string
# Number of consonants:  7
# Number of special characters:  1

vowel = 0 
cons = 0
spec = 0
special_characters = "!@#$%^&*()-+?_=,<>/" #specifying special characters tp be distinguished later
   
# .lower() converts user input to lower case, to more simply check vowels with a small array of characters. 
userInput = userInput.lower();  
for i in range(0,len(userInput)):   
    if userInput[i] in ('a',"e","i","o","u"):  #checks for vowels
        vowel = vowel + 1  
    elif (userInput[i] >= 'a' and userInput[i] <= 'z'):   #every letter from a - z, thats not a vowel
        cons = cons + 1  
    elif any(c in special_characters for c in userInput): #checks if input contains any of the special characters specified
        spec = spec + 1

print("Total number of vowels: ",vowel);  
print("Total number of consonants: ",cons);  
print("Total number of special characters: ",spec);  