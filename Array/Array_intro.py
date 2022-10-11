# introduction to array

# method 1 
import array

 # this will import entire array module

stu = array.array("i", []) # array.array("type code", [elements])
#arrayobject = modulename.classname("int", [element])

# method 2
from array import* # this will import all class, object , variable from array module

import array

stu = array.array("i", [1,2,43,5]) # integer values 
print(stu) 
print(type(stu)) 

stu1 = array.array('f', [1,2,3]) # f stands for float values 
print(stu1)
print(type(stu1))

from array import*

stu3 = array('i', [1,2,3,4,5])
print(stu3)
print(type(stu3))

# indesing is possible in array 
print(stu3[0]) # prints the first index element 

print('##############################################################')

#accessing array using for loop 
#without index
for i in stu3: # this will print all the element in the array stu3
    print(i)

#with indexing
for i in range(len(stu3)): # range function will help in printing the index for array
    print(i)

print('##############################################################')

#using while loop 
n = len(stu3)
i=0
while i<n:
    print(stu3[i])
    i+=1
print('##############################################################')

# getting input from user to store array using while loop
stu4 = array('i',[]) # empty array
n = int(input("How many element you want to add in array :- "))
i=0
while i<n:
    stu4.append(int(input("enter the element : - ")))
    i+=1
print(stu4)

print('##############################################################')

# methods in array 
# from numbers
# a=linspace(1,8)
# print(a)
# print(type(a))

