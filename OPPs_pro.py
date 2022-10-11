# from _typeshed import Self


# a = 10
# b = 20

# print ("the sum is ", a+b)

# this is precedural approach 

# oops approach 

# class name always in pascal case (first letter is capital)
class Number: # this class has a function which runs number objects
    def sum(self):
        return self.a + self.b

num = Number() # object instantiation for a new number .. naya instance banaya hai 
num.a = 10
num.b = 20
s = num.sum()
print (s)

# camel case means isNumeric or isFloat this is camel case 
