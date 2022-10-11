# lambda function in python is also known as anonymous function

# A lambda function can take any no of argument but can have only one expression
# example - sum = lambda a,b,c : a+b+c

# def func(a):
#     return a + 5

# lambda function syntax = lambda argument : expression 
                          #lambda a,b,c    : a+b+c

#using lambda functions 

func = lambda a: a+5 # function as argument passed, a will be the input and a+5 will be the argument
square = lambda a : a*a
sum = lambda a,b,c : a+b+c

x = 5
print (square(x))
print(func(x))
print(sum(1,2,3))


# lambda functions 
# functions created using an expression 
# lambda argument : expression 

'''
example 
    square = lambda X : X*X
    square (6) returns 36
    sim = lambda abc : a+b+c    1 or more expessions 
    sum (a,b,c) returns 6
'''
print("##########################")

#lambda function using one argument 
x = lambda a : a+10
print(f"The additon using lambda is {x(10)}")

# same programe using normal fucntion 

def add(a):
    return a+10
print(f"The addition using normal function is {add(10)}")

print("##########################")

print("########### Filter function ##################")
# Filter function will extract the value which matches the functionality and return it

val = [34,45,56,7,8]
def even_func(x):
    if x%2 == 0:
        return True
    else:
        return False

even = list(filter(even_func,val))
for x in even:
    print(x)

#same function using lambda with filter

val = [45,56,67,89,54,2]
even1 = list(filter(lambda i : i%2==0, val))
print(even1)
for x in even1:
    print(f"The even list using lambda function {x}")

even2 = [i for i  in val if i%2==0]
print(even2)

print("########## map function ##############")
#syntax of map function = map(fun, iter)
                         #map(function, (list,tuple,set)) 
# map function does the specified functionality with every element of the iter(list, tuple, dict)

# return double of numbers using map function 
def double(n):
    return n + n
numbers = [1,2,3,4]
result = list(map(double, numbers))
print (result) # output to be printed in list, tuple or set format 

#Double all numbers using map and lambda
result1 = map(lambda x :x+x , numbers)
print(list(result1))

print("############# Reduce function ##########")
# reduce function - [1,2,3,4] --> 1,2 are passed addition is done ,result 3 and 3 are passed ,additona is done, 
# result 6 and 4 are passed , additioa is done.
# syntax reduce (func, iter) --> reduce(function, (list,tuple,set))
# reduce function needs to be imported from functool 
# reduce functions passes first two values to perform some operation (additona, bugger, smaller etc) and 
# returns result which is compared with the next two values.

# program to sum of elements using reduce function 

from functools import reduce
def myfunc (a,b):
    return a+b
val = [1,2,3,4]
add = reduce(myfunc, val) # reduce takes function, iter as argument
print(f"Sum of elements using normal function {add}")

#same function using lambda 
add1 = reduce(lambda a,b : a+b, val)
print(f"Sum of elements using lambda function {add1}")

# fiunction to find the maximun number using reduce function 
def max_func (a,b):
    if a>b:
        return a
    return b
numbers = [2,5,6,9,1]
max = reduce(max_func, numbers)
print(f"The maximum no using normal function is {max}")

# same program using lambda function
max1 = reduce(lambda a,b : a if a>b else b, numbers)
print(f"The maximum no using lambda function is {max1}")


print("###############programe using filter, map and reduce function at same time ##############")
user = [14,15,16,17,18,19,20,21,22,43]
hard_worker = list(filter(lambda a : a > 18, user))
raise_10 = list(map(lambda a: a+10, hard_worker))
max_wage = reduce(lambda a,b: a if a>b else b, raise_10)
print(f"The maximum wage is {max_wage}")