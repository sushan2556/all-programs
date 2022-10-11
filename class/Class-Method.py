# same like static method there is an class method as well , which help us to change the class attribute

class Employee:
    company = "Camel"
    salary = 100 # class attribute 
    Location = "Delhi"

    # def changeSalary(self, sal):
        # self.salary = sal    # this will creat a instance attribute , self is for instance attribue
    
    # def changeSalary(self, sal):
        # self.__class__.salary = sal  # one way to change the class attribute 

    @classmethod # decorator, is a function takes and inout and modifies it 
    def changeSalary(cls, sal): # with the help of class method I can change the class attributes
        cls.salary = sal # class was accesses directly 

e = Employee()
print(e.salary)
e.changeSalary(450)
print(e.salary)
print(Employee.salary)