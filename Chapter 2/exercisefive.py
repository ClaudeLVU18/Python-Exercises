# Exercise 5: Count items☑️
# Write Python Program to Count the Number of Times an Item Appears in the List

staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Anmol","Zainab","Iftikhar", "Arshiya","Jake","Iftikhar"]

#declare variables as key for values of the individual elements
Count1 = staff.count("Arshiya")
Count2 = staff.count("Usman")
Count3 = staff.count("Iftikhar")
Count4 = staff.count("Anmol")
Count5 = staff.count("Zainab")
Count6 = staff.count("Jake")

#printing the total appearances of each element.
print(f"'Arshiya' appears a total of: {Count1} times.\n")
print(f"'Usman' appears a total of: {Count2} times.\n")
print(f"'Iftikhar' appears a total of: {Count3} times.\n")
print(f"'Anmol' appears a total of: {Count4} times.\n")
print(f"'Zainab' appears a total of: {Count5} times.\n")
print(f"'Jake' appears a total of: {Count6} times.\n")