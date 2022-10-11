 # Multilevel inheritance example

class Person:
    country = "India"
    def takeBreath(self):
        print("Im breathing")

class Employee(Person):
    company = "Honda"
    def getSalary(self):
        print(f"Salary is {self.getSalary}")

    def takeBreak(self):
        print("I'm emplyee and breathing..")

class Programmer(Employee):
    company = "Fiverr"
    def takeBreak(self):
        print("I' programmer and i'm breathing ..")

p = Person() # class object created 
e = Employee() # Employee class object created 
p.takeBreath()
pr = Programmer()
print(pr.country)

