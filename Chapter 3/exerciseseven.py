# Exercise 7: Lamda function☑️
# Create the list marks with the given values

marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]

#Using lambda function in the function sort the list elements of the tuple based on marks low to high and high to low    

marks = tuple(sorted(list(marks), key=lambda x: x[1]))

print("\nLow to High:",marks)
marks = tuple(sorted(list(marks),reverse=True, key=lambda x: x[1])) #reverse = true is used to reverse the sorting to High To Low
print("\nHigh to Low:",marks)
