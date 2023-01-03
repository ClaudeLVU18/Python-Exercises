# Exercise 4: Petrol Price ☑️
# Every time a motorist buys some petrol, he notes the number of liters bought and the amount paid per liter. This data can be found in the petrolPrice.txt file in your GitHub repository.The data is stored in columns separated by a tabbed space, like the following sample:

# Liters	cost
# 20.0	  56.40
# 9.6	  29.95
# 5.0	  15.60
# 15.0	  54.30
# 18.4	  65.32
# 18.7	  75.36
# 17.7	  80.00
#     Write a program that calculates:

# What was the overall average price per litre of petrol bought?
# How much petrol in litres was bought at under 3.5AED per liter?

# Create a list with the for petrol liter, cost, and price per liter
liters = [20.0, 9.6, 5.0, 15.0, 18.4, 18.7, 17.7]
cost = [56.40, 29.95, 15.60, 54.30, 65.32, 75.36, 80.00]
per = []

# go through the elements of the liters and cost lists and divide them to get per price value
for i in range(len(liters)):
    result = cost[i] / liters[i]
    per.append(result)

#display every list we have so far
print("Liters:")
for x in liters:
    print(x)
print("\nCost:")
for x in cost:
    print(x)
print("\nPrice per liter:")
for x in per:
    print(round(x, 2))

#formula to find the average by using the indexes of the results of liters / cost
sum_ = sum(per)
length = len(per)
average = sum_ / length #separate variable created for the average so it may be rounded off
print("\nThe average price per litre of petrol bought was:", round(average, 2)) #rounded off the average to 2 decimal places

cheap = 0

#exact same procedure in finding cost per liter, but now, for every result under 3.5, take that index value and add them together
for i in range(len(liters)):
    result = cost[i] / liters[i]
    #for every cost per liter now an if statement is used to identify all indexes whose result is under 3.5
    if result < 3.5:
        cheap += liters[i]

print("The total amount of liters that could be bought for under 3.5 is: ",cheap)



