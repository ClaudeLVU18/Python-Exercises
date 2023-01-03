# Optional Exercise 6: Locations List
# Using the list

locations =['Dubai','Paris', 'Switzerland', 'London', 'Amsterdam', 'New York']

# Print the list and find the length of the list
print("List: ", locations, "\nLength:", len(locations))

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print("\nAlphabetically temporarily arranged: ",sorted(locations))

# Show that your list is still in its original order by printing it.
print("\nOriginal list: ",locations)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
print("\nAlphabetically temporarily arranged descendingly: ",sorted(locations, reverse=True))

# Show that your list is still in its original order by printing it again.
print("\nOriginal list: ",locations)

# Use reverse() to change the order of your list.
locations.reverse()

# Print the list to show that its order has changed.
print("\nReversed order: ",locations)

# Use sort() to change your list so it’s stored in alphabetical order.
# Print the list to show that its order has been changed.
locations.sort()
print("\nAlphabetically permanently arranged: ",locations)

# Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.   
locations.sort(reverse=True)
print("\nAlphabetically permanently arranged descendingly: ", locations)