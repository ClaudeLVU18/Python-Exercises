class Animal:
    def __init__(self, type, name, colour, age, weight, noise):
        self.type = type
        self.name = name
        self.colour = colour
        self.age = age
        self.weight = weight
        self.noise = noise

    #declaring the requested methods
    def sayHello(self):
        print(f"\nHello, my name is {self.name}.")

    def makeNoise(self):
        print(self.noise)

    def animalDetails(self):
        print(f"Animal Type: {self.type}")
        print(f"Name: {self.name}")
        print(f"Colour: {self.colour}")
        print(f"Age: {self.age} years old.")
        print(f"Weight: {self.weight} lbs")
        print(f"Noise: {self.noise}")


# create two Animal objects
cat = Animal("Cat", "Fiona", "White", 1, 8, "Meow!\n")
monkey = Animal("Monkey", "Jonathan", "Brown", 5, 15, "Oooh! Aaah!\n")

cat.sayHello()
cat.makeNoise()
cat.animalDetails()

monkey.sayHello()
monkey.makeNoise()
monkey.animalDetails()