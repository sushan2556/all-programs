# encapsulation in python - How the method will work , implementation will work 
# wrapping of data under single unit 
# variable and data are hidden in the class shield 
# example - capsule - methods and variables are hidden inside the capsule 
# wending machine 
# benefits - data hiding, Flexibility (read only, write only), reusablity 
# abstraction - details in the data only the usefull data , hiding everything from you 
# encapsulation is hiding the internal working 

# how encapsulation is used in Python 
# plain attrubutes are used in order to achieve encapsulation
# Access specifier - private and public  
'''
Double underscore                        Single underscore 
__name                                 _name
__method()                             _method()

A Class in Python has three types of access modifiers:

Public Access Modifier
Protected Access Modifier
Private Access Modifier

'''
print ('--------------------------------------------------------------------')
class Edureka: 
    def __init__(self):
        # declared two varibales one is public other is private
        self.course = "basics of Python " # public attribute/variable
        self.__tech = "Python" # private attribute/varibale by using __

    def coursName(self):
        return self.course + self.__tech
oj = Edureka()
# print(oj.__tech)
# print(oj.course) # this will not access the priviate members 
# print(oj.coursName())
# oj.coursName() # can access inside the class 

# trying to access the private attribute using name mangling 
# name mangling is used for private data members 
# print(oj._Edureka__tech)
print ('--------------------------------------------------------------------')
print("######### getter setter ##################")
class Radhe_Institute():
    def __init__(self):
        self.course = "Python Basics"
        self.__tech = "Python"

    def show_course(self):
        return self.course + ":"+ self.__tech
    def set_tech(self, x):
        self.__tech = x
    def get_tech(self):
        return self.__tech

obj = Radhe_Institute()
# print(obj.show_course())
# print(obj.get_tech())
obj.set_tech("Python library")
print(obj.get_tech()) # use it to know the private variable

# restricting of data access using function is called encapsulation 
print ('--------------------------------------------------------------------')
# Second example for encapsulation 

class Car: # created speed class which has 2 parameter defined , speed and colour
    def __init__(self,colour, speed): # contructor created 
        self.__speed = speed
        self.colour = colour

    # setter and getter method
    def set_speed(self,value): 
        self.__speed = value
    def get_speed(self):
        return self.__speed

ford = Car('Red', 100) # first object instantiation 
ford.set_speed(112)

# ford.speed = "slow" # illogical inputs , important to protect the data

# print(ford.colour)
print(ford.get_speed()) # this will return the value that was set in line 75
# even if we create a set and get method , the data is not protected . we can change it 
# in this case we will make the data as protected 
# print(ford.speed) # when we try to access the protected data of the class 
# when the variable is private we need to set the speed using the setter method 
print ('--------------------------------------------------------------------')
# third example for encapsulation 

class Rectangle:
    def __init__(self,height,width):
        self.__height = height # create the variable as private
        self.width = width
    
    def set_height(self,other): # creating set method , to access and update the provate data members
        self.__height = other 
    
    def area(self):
        return self.__height * self.width

rect1 = Rectangle(2,3)
rect1.height = 3 # this changes the data of my rectangle , to avoid doing so we 
rect1.__height = 3 # even if we try to set the value in this way it wont set
rect1.set_height(3) # we can set the value of height using the setter method 
print(rect1.area())

rec1 = Rectangle(3,6)
rect2 = Rectangle(2,4)

print ('--------------------------------------------------------------------')
# Python encapsulation example 

class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current
    
    def reset(self):
        self.__current = 0

counter = Counter() # created a counter object for couneter class 
counter.increment()
counter.increment()
counter.increment()

counter.current = -999 # assigning invalid value
# to avoid this , we can declare the variable as private 

print(counter.value())

#name mangling in encapsulation 
counter._Counter__current = 1 # this was we can change the value of the private data member 
print(counter.value())
print ('--------------------------------------------------------------------')
