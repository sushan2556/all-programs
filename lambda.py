# def func(a):
#     return a + 5

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