# Method overriding in python
class Bird():
    def walking (self):
        print("I can walk")
    def flying(self):
        print("I can fly")
class Penguin(Bird):
    def flying(self):
        print("I cannot fly")
p = Penguin()
p.flying() # method overriding using inheritance

# python duck typing
class Pycharm:
    def execute(self):
        print("compailing")
        print("Running")
class VScode:
    def execute(self):
        print("Compailing")
        print("Running")
        print("Spell check")
class laptop:
    def code(self,ide):
        ide.execute()
ide = VScode()
lapt1 = laptop()
lapt1.code(ide)

#duck typing second example
class duck:
    def walk(self):
        print("chapak chapak ")
class horse:
    def walk(self):
        print("thbdak thabdak")
class cat:
    def talk(self):
        print("Meow meow")

def myfunction(obj): # creating a function which will take obj as an argument
    obj.walk()

h=horse()
myfunction(h)
d=duck()
myfunction(d)
c=cat()
# myfunction(c)

#duck typing second example

class Aeroplane:
    def fly(self):
        print("fly with fuel")
class Bird:
    def fly(self):
        print("fly with wings")
class Fish:
    def swin(self):
        print('Swims with fins')

def myfunction(obj): # creating a function which will take object as an argument
    obj.fly()

b = Bird()
m = myfunction(b)
f=Fish()
# myfunction(f) # fish object does not have the attribute fly

# duct typing


# method overloading
class main_class:
    def base_function(self,x=None,y=None,z=None):
        if x==None and y==None and z==None:
            print("No argument pass")
        elif x!=None and y==None and z==None:
            r = 1
            for i in range(x,x+1):
                r = r*i
                print(i)
        elif x!=None and y!=None and z==None:
            print(x+y)
        else:
            print(x*y*z)

obj1 = main_class()
obj1.base_function(2,2)
obj1.base_function()
obj1.base_function(2,2,2)

#second example
class greeting:
    def to_greet(self,name=None):
        if name!=None:
            print("Good Morning ", name)
        else:
            print("Good Morning !")
greet = greeting()
greet.to_greet()
greet.to_greet("Sushant")

print("############ operator overloading ##############")
a=10
b=20
print(a+b)
print(int.__add__(10,20)) # this is what happens in the background

# lets say we have a class of emplpoyee # Operator overloading
class Employee:
    def __init__(self,salary):
        self.salary = salary
    def __add__(self,other):
        return self.salary + other.salary
    def __mul__(self,other):
        return self.salary * other.salary

emp1 = Employee(100)
emp2 = Employee(200)

emp3 = emp1*emp2 # this will tell us that operator + is not defined in class Employee
print(emp3) # this was executed as we defined the add method above in line no 115

# Method overloading example
class Sum:
    def adding(self, x,y):
        sum = x+y
        print(sum)
    def new_adding(self,x=None,y=None,z=None):
        if x!=None and y!=None and z==None:
            print(x+y)
        elif x!=None and y!=None and z!=None:
            print(x+y+z)

s = Sum()
s.adding(2,2)
# s.adding(2,2,2) # we cannot pass 3 arguments
s.new_adding(2,2)
s.new_adding(2,2,2)


