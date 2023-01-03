# Exercise 1: Woof Woof ☑️
# Write a program that declares a class which defines the characteristics of a dog. 


#declaring class and functions
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def woof(self):
        print("Woof!")


# The program should instantiate two objects from this class and assign data to its members. 
dog1 = Dog("Buddy", "Labrador", 3)
dog2 = Dog("Daisy", "Beagle", 5)

# The program should then output the data from each object and the oldest dog should woof via a class method.
print(f"{dog1.name} is a {dog1.breed} and is {dog1.age} years old.")
print(f"{dog2.name} is a {dog2.breed} and is {dog2.age} years old.")
if dog1.age > dog2.age:
    dog1.woof()
else:
    dog2.woof()
