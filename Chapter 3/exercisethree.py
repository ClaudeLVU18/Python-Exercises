# Exercise 3: Area Function☑️
# Code a program to display a menu on the screen that asks if the user wants to

# 1: Calculate the area of a square
# 2: Calculate the area of a circle
# 3: Calculate the area of a triangle 


#functions are defined with their respective formulas in finding each area
def circCalc(radius):
    pi = 3.14
    area = pi*radius
    return area

def sqrCalc(side):
    area = side*side
    return area

def triCalc(b,h):
    area = .5*b*h
    return area

print("\nSelect a desired shape to calculate the area of:\n")
print("1.Calculate the area of a square")
print("2.Calculate the area of a circle")
print("3.Calculate the area of a triangle")

userinp = int(input("\nSelect the number of your choice: "))

if userinp == 1:
    sides = float(input("Enter the sides of your square: "))
    print(sqrCalc(sides))
elif userinp == 2:
    rad = float(input("Enter the radius of your circle: "))
    print(circCalc(rad))
elif userinp == 3:
    base = float(input("Enter the base of your triangle: "))
    height = float(input("Enter the height of your triangle: "))
    print(triCalc(base,height))
else:
    print("ERROR: not a valid selection")
    