#procedural oriented programing
a = 12
b = 34

print("The sum of a and b is ", a+b)


# oops example 
# class is a blueprint
class Number:   #initial letter in capital for class in (pascal case - Number) Camel case (isNumeric) 
     def sum(self):
         return self.a + self.b

num = Number() # object instantiation
num.a = 12
num.b = 34
s = num.sum()
print(s)


'''
class means template it is a blueprint
if class is railway form than application is object

class has information to create valid object 
object needs to instaciate to create a object in class

class Employee:
    # methods and variables

an Object is an instanciation of class. When class is defined , a template (info) is defined. Memory is allocated only
after object instantiation.

'''

class Test:     
    def _init_(self):
        self.a=10 
        self.b=20
    def m1(self):   
        self.c=20
t=Test()
print(t)

class Person():
    def __init__(self, name, age): 
        self.name = name # instance variable defined
        self.age = age
    def Greeting(self): # inserted a greeting function in the class
        print(f"hello my name is {self.name} and my age is {self.age}")

p1 = Person("Sushant", 35) # p1 oject created of the class , for every object the instance variable is different
print(p1.name) 
print(p1.age)
    
p2 = Person("Shweta", 30)
print(p2.Greeting())
