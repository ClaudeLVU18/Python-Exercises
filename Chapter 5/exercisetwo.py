# Create a class called students.

# The class should have the following members.Name (string), Mark1 (int), Mark2 (int), Mark3 (int) 
# The class should have the following methods calcGrade() - should return an average from the three marks.display()- should output the student name and calculated grade average
# Create one object using a constructor that contains parameters to initialise all of the variables
# Ask user to input the variable values using input() and pass the values to the second object

class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def avg(self): #method to find grade average
        return (self.mark1 + self.mark2 + self.mark3) / 3

    def display(self):
        print(f"{self.name} has an average grade of {self.avg():.2f}.") #using recursion, the average is found

name = input("Enter the name of the student: ")
mark1 = int(input("Enter the first mark: "))
mark2 = int(input("Enter the second mark: "))
mark3 = int(input("Enter the third mark: "))

#declaring student using constructor 
student = Student(name, mark1, mark2, mark3)
student.display()
