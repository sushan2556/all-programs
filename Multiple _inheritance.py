# multiple inheritance 
# when child class has more than two parents
# Child -->> Dad class -->> Mom Class
''''
        Parent 1          parent2
            |_              _|
                    |
                Child 

'''
#example Multiple Inheritance
class Employee():
    company = "Visa"
    eCode = 120

class Freelancer(): #Parent class
    company = "Fiverr"
    level = 0

    def upgradeLeval(self):
        self.level = self.level+1

class Programmer(Employee, Freelancer): # all attri from Emplyee and Freelancer class 
    name = "Sushant"

p = Programmer()
p.upgradeLeval()
print(p.level)
print(p.company) # this will print visa first as class programmer takes Employee attributes first and Freelancer second 
# over here "Programmer(Employee, Freelancer)"
# whichever class is written first it will be given the priority 