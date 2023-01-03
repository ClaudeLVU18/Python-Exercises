class Employee:
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

    def setData(self):
        self.name = input("Enter the name of the employee: ")
        self.age = int(input("Enter the age of the employee: "))
        self.id = input("Enter the ID of the employee: ")
        self.salary = float(input("Enter the salary of the employee: "))

    #in order to meet the specified expected output stated in the GitHub excercise, we must arrange the employee info in a column
    #based off my research in python, this can be achieved by using 'ljust' and 'rjust' these commands add spacing with the use of a certain
    #character, but if no character is specified, the default character is and empty space, followed by the number of times
    #we want the function to be used.
    def getData(self):
        print(self.name.ljust(15), self.id.ljust(8), str(self.age).ljust(6), "{:.2f}".format(self.salary).ljust(10))



# create an empty list of employees
employees = []

# create 5 Employee objects and append them to the list
for i in range(5):
    employee = Employee("", 0, "", 0.0)
    print(f"\nEnter the details for Employee {i+1}:\n")
    employee.setData()
    employees.append(employee)

# print the data for each employee
print("Name".ljust(15), "id".ljust(8), "Age".ljust(6), "Salary".ljust(10))
for employee in employees:
    employee.getData()
