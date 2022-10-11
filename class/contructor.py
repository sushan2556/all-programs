# __init__ is the first method that is run when an object is created 
# it takes self argument as well as further argument class Employee:
class Employee:
    company = "Google" # class attribute

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created") 
        # this method will automatically run. This is called contructor as it initialize and object

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"Thge salay for Sushant is {self.salary} and company is {self.company}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning Sir")

sushant = Employee("sushant", 1000, "coder")
sushant.getDetails()