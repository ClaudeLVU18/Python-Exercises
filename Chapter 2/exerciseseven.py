# Optional Exercise 7:Cities Dictionary
# Make a dictionary called cities. 
# Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city
# and include the country that the city is in, its approximate population, and one fact about that city. 
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.

perthCity = {"Country": "Australia", "Population" : "2.5 million", "Fact": "Perth is home to the largest inland park in the world."}
dubaiCity = {"Country": "UAE ", "Population" : "3.49 million ", "Fact": "Dubai has the world's tallest building."}
moscowCity = {"Country": "Russia", "Population" : "13 million ", "Fact": "It's home to a haunted embassy."}

cities = {"Perth": perthCity, "Dubai": dubaiCity, "Moscow": moscowCity} # cities dictionary with dictionaries as their values

for i in cities:
    print(i,":", cities[i])