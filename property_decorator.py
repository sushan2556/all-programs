class Employee:
    company = "bharatGas" # class
    salary = 5600  # class property or attribute
    salarybonas = 400

    @property # getter method  
    def totalSalary(self):
        return self.salary + self.salarybonas

    @totalSalary.setter  # setter is a decorator 
    def totalSalary(self, val):
        self.salarybonas = val - self.salary
    
e = Employee()
print(e.totalSalary)
e.totalSalary = 5800 # this will call the setter method
print(e.salary)
print(e.salarybonas)

'''
getter syntax 

class Employee()
    @property
    def name (Self)
        return self.ename

setter syntax

    @name.setter
    def name (self, val)
        self.ename = val

'''