# Exercise 3 : Film Dictionary☑️
# Create a dictionary that contains relevant data for films (e.g. Title, Director, etc). Display the film details using loop

#declaring the film's details
films = {"Title": "Avatar", "Director": "James Cameron", "Year Released": 2009, "Budget": "237 million USD"}

#simple for loop to neatly display dictionary contents. index value is used to display both value and title places.
for i in films:
    print(i,":", films[i])