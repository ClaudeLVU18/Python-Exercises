# Exercise 4: Shapes ☑️
# Create a parent class called shape. This should have following methods inputSides() – 
# Ask user to enter the sides of the shape. Now create subclasses for a circle, rectangle and triangle. 
# These should include an appropriate area() method that will use the side values from the shape class.    

#the math library is requested by calling the module math. This allows for the use of the 'pi' function
import math

#defining the parent class - Shape
class Shape:
    #the constructor method, which is ran whenever this class is being claled
    def __init__(self, sides):
        self.sides = sides
    #a method to request user for number of sides, and display what shapes align with the number of sides they input
    def inputSides(self):
        print("Circle = 0 sides\nRectangle = 4 sides\nTriangle = 3 sides")
        self.sides = int(input("Enter the number of sides of your desired shape: "))
        
#creating subclasses for each shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    #defining the formula to find the area of a circle
    def area(self):
        self.radius = float(input("Enter the radius of the circle: "))
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
#defining the formula to find the area of a circle
    def area(self):
        self.length = float(input("Enter the length of the rectangle: "))
        self.width = float(input("Enter the width of the rectangle: "))
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
#defining the formula to find the area of a circle
    def area(self):
        self.base = float(input("Enter the base of the triangle: "))
        self.height = float(input("Enter the height of the triangle: "))
        return self.base * self.height / 2

#an instance that calls the parent class shape is created in order to be used as a variable later on
shape = Shape(0)
shape.inputSides()

#performs area calculations based on shape selected which is defined by the number of shapes the user has inputted
if shape.sides == 0:
    s = Circle(0)
    print(s.area())
elif shape.sides == 4:
    s = Rectangle(0, 0)
    print(s.area())
elif shape.sides == 3:
    s = Triangle(0, 0)
    print(s.area())
else:
    print("Invalid number of sides")


