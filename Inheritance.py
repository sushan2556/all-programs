
'''
********** Inheritance is the way of creating new class from an existing class **********

----------
suntax

class Employee: # base class 
    # code

class Programmer (Employee): # derived or child class
    # code

uses the DRY principle .... loops uses dry principle 
----------

with the help of inheritance we can derive a new class from the base class

'''
# Single inheritance example
class Employee: # parent class / base class
    company = "Google"
    def showDetails(self):
        print("This is an google employee")
    
class Programmer (Employee): # child class / derived class 
    # company = "Youtube" 
    def showDetails(self):
        print("This is an youtube employee")

e = Employee()
# e.showDetails()
print(e.company)
p = Programmer()
# p.showDetails()
print(p.company)
# add attributes in programmer class

'''

types of inheritance

Single inheritance - 
when child class inherites only parent class

Multiole -


Multilevel 


'''