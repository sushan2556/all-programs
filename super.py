class Person:
    country = "India"
    def takeBreath(self):
        print("Im a person and I'm breathing")

class Employee(Person):
    company = "Honda"
    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("Im employee and I'm still breathing")

class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print("No salary to programmer")
    
    def takeBreath(self):
        super().takeBreath() # this will run the take breath function from the super class which is class=Person
        print("Im a Programmer so I'm breathing..")
    
p = Person() # object created 
p.takeBreath()

e = Employee() # object create kela 
e.takeBreath()

pr = Programmer()
pr.takeBreath()

