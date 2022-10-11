# methods in the class 
# regular method, clas methods, ststic methods 
# reg = instance as first argument (self) , class method is use to change reg method to class method 
# using decorator
from calendar import weekday


class Employee:
    # class varibales 
    no_of_emps = 0
    raise_amt = 1.04
    def __init__(self, fname, lname, pay): # Class init method # Contructor
        self.fname = fname
        self.lname = lname
        self.pay = pay
        Employee.no_of_emps += 1
    # fullname function
    def fullname(self): # method to find full name of the employee
        return '{} {}'.format(self.fname,self.lname)
    #Apply raise function 
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    @classmethod # using class method to change the value for raise
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    @classmethod # converting the string passes into variables 
    def from_str(cls,emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname,lname,pay)
    @staticmethod # line 54
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

print(f"The no of emplyees at begining are : - {Employee.no_of_emps}")
emp1 = Employee('Sushant','Jadhav',75000)
emp2 = Employee('Shweta','Jadhav', 65000)
print(emp1.fname)
print(emp2.fname)
print(Employee.no_of_emps)
emp3 = Employee('test', 'user', 10000)
print(emp3.fullname())
emp1.apply_raise()
print(emp1.pay)
print(f"The Employee raise at begining is {Employee.raise_amt}")
Employee.set_raise_amt(1.05) # change the class variable using class method
print(f"The Employee raise after update is {Employee.raise_amt}")
# what if the fname lname and pay is passed through a string 
new_emp_str = "Test2-user2-20000"
new_emp1  = Employee.from_str(new_emp_str)
print(new_emp1.fullname())

import datetime
my_date = datetime.date(2022,7,31)
print(Employee.is_workday(my_date)) #static method to check the workday