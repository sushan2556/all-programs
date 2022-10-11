class Employee:
    company = "Google" # class attribute

    def getSalary(self, signature):
        print(f"Thge salay for Sushant is {self.salary} and company is {self.company}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning Sir")


sushant = Employee()
sushant.salary = 100
# sushant.company = "youtube" # company instance attribute
sushant.getSalary("Thanks!")
sushant.greet() 
