#changing from one form to other form is called polymorphism , one thing many ways 
# there are 4 ways of achieving polymorphism in python
# Duck typing
# Operator overloading (+ , _, * , /) we use the method which are .__add__ 
# Method overloading
# Method overriding

'''
'''
#Python doesn't care about which type of object it is . in order to call an existing method on an object .
# if the method is defined on the object , then it will be called.
# it if walks like a duck , talks like a duck it is a duck 
# it does not matter which class of object it is , if it is an object and required beheviour is present then it will work
# practising duct typing 
class pyCharm:
    def execute(self):
        print("Compiling")
        print("Running")
class myEditor:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Spell check")
class laptop:
    def code(self,ide):
        ide.execute()
ide1 = pyCharm()
# first we had the pycharm ide and now if we change it to different IDe , it will still work provided it should
# have execute method

ide1 = myEditor()
# changing the ide to myeditor which has same method as pycharm .
# this is called duck typing 

lap1 = laptop()
lap1.code(ide1) # type of ide is pyCharm, it is not fixed and we can change it to myEditor

# second example 
class duck:
    def walk (self):
        print("thapak thapak")
class horse:
    def walk(self):
        print("thabdak thabdak")
class cat:
    def talk(self):
        print("Meow Meow")
def myfunction(obj): # it does not matter whcih class object it has received , it will execute the walk method
    obj.walk()
h = horse()
myfunction(h)
d = duck()
myfunction(d)
c = cat()
# myfunction(c) # cat object does not have the method walk, hence it will not work.
# second example 
class duck:
    def sound(self):
        print("quak quak")
class cat:
    def sound(self):
        print("Meow")
class human:
    def sound(self):
        print("Hello")
class test:
    def invoke(self,obj):
        obj.sound()
t = test()
obj_1 = duck()
t.invoke(obj_1)
obj_1 = cat()
t.invoke(obj_1)
obj_1 = human()
t.invoke(obj_1) # it does not matter if the object is of which class, unless it has the sound method in it

# Second Pillar of operator overloading 
# same method of operator , the argument are different 
'''
5+6 = + is operator 
Hello + worl = Hello world 
'''
a = 5
b = "world"
# print(a+b) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
a = 5
b = 6
print(a+b)
print(int.__add__(a,b)) # this is being called in the background)
# if we make them string 
a = "Sushant"
b = "Jadhav"
print(a + b)
print(str.__add__(a,b)) # inbuild class does not have 2 things toghether , int and str 

class student:
    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3

    def __gt__(self,other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1 > s2:
            return True
        False
    def __str__(self):
        # return self.m1,self.m2 # this will print with the print(s1.__str__()) method and not with print(s1)
        return (f"{self.m1} {self.m2}")  # this was we can use print(s1) by putting it in string format
    
s1 = student(50,60)
s2 = student(40,45)

s3 = s1 + s2 # here I want a new student with additon marks of both s1 and s2 # defined it at 100
# + opeator with objects error 
#TypeError: unsupported operand type(s) for +: 'student' and 'student'
print(s3.m1, s3.m2)
# if we have to add two student we need to overload the operator of + , class does not know what plus is,
# we need to define the add method here

if s1 > s2: # > operator not working in python  # defined the method at 106
    print("s1 wins")
else:
    print("s2 wins")

a = 1 
print(a) # this will print the value of a 
# print(s3) # this will print the address of s3 --> <__main__.student object at 0x000001DC9BB77BB0
# whenever we try to print the object , behind it is calling mwthod as str method 
print(a) # is calling 
print(a.__str__()) # we need the value and not address , override the method defined at 112
# print(s1.__str__()) # overide the method to return values at line 112
print(s3)

# Method overloading in polymorphism 
# A function can be called with different number of argument 
# python does not support method overloading by default. But there are different ways to achieve method overloading in Python. 
# Methods in Python can be called with zero, one, or more parameters. This process of calling the same method in different 
# ways is called method overloading.
# advantages - reduces complexities , Reusability , accesibility 
print("##################################")
class main_class:
    def base_function(self,x=None,y=None):
        if x==None and y==None:
            print("No arguments passed")
        elif x!=None and y==None:
            f = 1
            for i in range (x,x+1):
                f = f*i
                print(f)
        else:
            print(x+y)

obj1 = main_class() 
obj1.base_function() # function was called with no arguments  
obj1.base_function(12) # function was called with 1 argument 
obj1.base_function(12,13) # function was called with 2 arguments

# second example of method overloading 
class greetings:
    def to_greet(self, name=None):
        if name != None:
            print("Good Morning " + name + ' !')
        else:
            print("Good Morning !")

obj3 = greetings()
obj3.to_greet() # same function called with 0 argument 
obj3.to_greet('Sushant') # same function called with one argument 
# methods in python can be called with zero, one or more parameter , this process of calling same method with different parameter 
# is called method overloading


# Method overriding 
# Method overriding works with inheritance 
# if we write method in both clases, parent class and  child class then the present method is not avalable in child class 
# in this case only child class method is accesible which means child class methos is replacing parent class method 
# method overriding is used when programmer want to modify the existing behaviour of a method 
class add:
    def result (self,a,b):
        print("Additon : ",a+b)

class multi(add):
    def result(self,a,b):
        super().result(2,2) # pass the parameter over here
        print('Multiplication :',a*b)

obj4 = multi()
obj4.result(2,2) # this called the result method from the multi class and not from add class 

#if i create a object of add class , then it will run the result method from the add class 
obj5 = add()
obj5.result(2,2) # result method of addition function is called from the add class

# inheritance is used so that we can work with the parent class object 
# In method overriding if we still want to use the method from the parent class we can use the super method 
# we use inheritance so that we can do the function using child class and no need to create an extra object of the parent class
# super method is use to call parent class methods or contructor # added in line 191
# second example for method overriding 
class Bird:
    def flying (self):
        print("I can fly")
    def walking (self):
        print("I can walk")
class Sparrow(Bird):
    pass
class Penguin(Bird):
    def flying(self):
        print("I cannot fly")
s=Sparrow()
s.flying()
p=Penguin()
p.flying()
