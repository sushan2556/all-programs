'''
######### DECORATOR ###################

#Decorators are nothing but functions that add new functionalities 
to the existing methods without changing them.

#A decorator takes in a function, adds some functionality and returns it.

# decorator is meta programming i.e. part of program tries to modify another part of program 

we must know few things:
To understand Decorators, you need to understand functions in Python, 
functions are first-class objects i.e we can assign multiple variables to the same function 
or we can even send them as arguments to other functions.

1)  Various different names can be bound to the same function object.
ex: here below names two and one refers to same function object
'''

def one(msg):
    print(msg)

one('Welcome')
two = one
two('Welcome')
del(one)
two('this is pyhton')

'''
2) Functions can be passed as arguments to another function.

Such functions that take other functions as arguments are also called higher order functions
'''
print('------------------------------------------------------------------------')
def increment(x):
    print('increment of ',x,'=',x + 1)

def decrement(x):
    print('decrement of ',x,'=',x - 1)

def calculate(func, x):
    return func(x)

calculate(increment,1)
calculate(decrement,5)
###################################################################

def lower_case(txt):
    return txt.lower()

def upper_case(txt):
    return txt.upper()

def format_txt(func):
    text = func('Hello Everyone...')
    print(text)

format_txt(lower_case)
format_txt(upper_case)

######################################################################
'''
3) A function can return another function.
'''
print('-----------------------------------------------------------')
def calculation():
    def addition(x, y):
        print('Addition of ',x,' and ',y,' = ', x + y)
    return addition

add = calculation()
add(3,5)

##############################################################################
'''
When to Use a Decorator in Python

* You'll use a decorator when you need to change the behavior of a function 
without modifying the function itself. 

* You can also use one when you need to run the same code on multiple functions. 
This avoids you writing duplicating code.

Syntax: 
def my_decorator_func(func):

    def inner_func():
        # Do something before the function.
        func()
        # Do something after the function.
    return inner_func
'''

def upper_case(func):
    def inner_func(txt):
        #return txt.upper()
        func(txt.upper())
    return inner_func

@upper_case
def print_txt(txt):
    print(txt)

print_txt('WelCome')
# str = print_txt("Welcome to python")
# print(str)

upper_case(print_txt('python program'))
#print(dec1('python program'))



print('------------------------------------------------------------')

def smart_div(func):
    def inner(a,b):
        print("I'm dividing ",a,"and",b)
        if(b==0):
            print('We cannot divide by 0')
            #return
        else:
            func(a,b)
    return inner
@smart_div
def Division(a,b):
    print('Division = ',a/b)

Division(4,0)
Division(40,4)
# print(division.__name__)

print('------------------------------------------------------------')

# Decorator that prints name of function before it runs
def func_name_printer(func):
    def wrapper(*args):
        print("Function that started running is " + func.__name__)
        func(*args)
    return wrapper

@func_name_printer
def add(*args):
    tot_sum = 0
    for arg in args:
        tot_sum += arg
        print("result = " + str(tot_sum))
    #print(add.__name__)

@func_name_printer
def sub(*args):
    tot_sub = args[0]-args[1]
    print("result = " + str(tot_sub))

@func_name_printer
def mul(*args):
    tot_mul = 1
    for arg in args:
        tot_mul *= arg
        print("result = " + str(tot_mul))

add(1,2,3,4)
mul(1,2,3)
sub(400, 150)


#Timer: Decorator Track time taken by a function to run.
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        print("Tracking function: " + func.__name__ + "()")
        start = time.time()
        print(start)
        func(*args, **kwargs)
        end = time.time()
        print(end)
        print("Time taken by the function to run is " + str(end-start) + ' sec')
    return wrapper

@timeit
def looper(*args, **kwargs):
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")
    for loop in kwargs.values(): 
        print(loop)

looper(2, 3, 4, loop1=10, loop2=11, loop3=12, loop4=15)
print('-----------------------------------')

prime_list = []
@timeit
def find_prime_number(list1):
    for num in list1:
        if num > 1:
            for j in range(2,num):
                if num % j == 0:
                    print(num,' is not prime number')
                    break
            else:
                print(num," is prime number")
                prime_list.append(num)

    print("prime numbers are : ",prime_list) 
list_numbers = [3,56,34,23,13,45,50,1]
find_prime_number(list_numbers)

print('------------------------------------------------')
@timeit
def addition(*args):
    sum = 0
    for num in args:
        sum += num
        print('Adition of',args,' = ',sum)
addition(100,200,300,400,500,600,700,800,900)

print('-------------------------------------------------')
@timeit
def range_addition():
    sum = 0
    for n in range(101):
        sum += n
    print('sum of 1 to ',n, " = ", sum)
range_addition()
print('-------------------------------------------------')

'''decorator chaining - multiple decorators to single function'''
def star(func):
    def inner(msg):
        print("*" * 30)
        func(msg)
        print("*" * 30)
    return inner

def percent(func):
    def inner(msg):
        print("%" * 30)
        func(msg)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer("Hello")