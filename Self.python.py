class  Employee:
    company = "Google"
    def getSalary(self):
        print(f"The salary is {self.salary} {self.company} ")

sushant = Employee()
sushant.salary = 100
sushant.getSalary()
# Employee.getSalary(sushant)

Shweta = Employee()
Shweta.salary = 300
Shweta.company = "Youtube"
Shweta.getSalary()
# Employee.getSalary(Shweta)
