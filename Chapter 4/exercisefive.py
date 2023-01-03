# Exercise 5: letter count ☑️
# Write a program that reads the contents of the sentences.txt file and counts the occurrences of each letter.

with open('sentences.txt', 'r') as f:
    # .read() is used to read the contents as it is more appropriate for we are counting the total number of letter occurences
    #for the whole file, as opposed to using readline() where it reads per line it is unneccessary for this program
    contents = f.read()

# A dictionary is used to store the counts of each letter
letter_counts = {}
for char in contents:
    # increment letter count per iteration
    if char.isalpha():
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

# sort the letters by alphabetical order
for letter in sorted(letter_counts.keys()):
    # print the letter counts
    print(f'{letter}: {letter_counts[letter]}')
