# Operator overloading these methods are called when a given object is called
# this are also called dunder methods 

class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self,num2): # __add__ is a method to do addition 
        print("Lets add")
        return self.num + num2.num
    def __mul__(self,num2): # __mul__ is a method to do multiplication 
        print("Lets Multiple")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)

'''
for add              -  __add__
for Multiplication   -  __mul__
for substraction     -  __sub__
for divide (/)       -  __truediv__
for //               -  __floordiv__

'''