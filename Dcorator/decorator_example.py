# decorator function example 

def decor(num):
    def inner():
        print("If : Before enhancing the function")
        num()
        print("If : After enhancing the fubnction")
    return inner

def num():
    print("We will use the this function ")
    print("and will enhance this in decorator")

num = decor(num)
num() # from here the python interpretor willgo to line no 4

# I need to add more print in this function without modifying the print statement in num()
# decorator will use this function and enhance this and return 
# our purpose is to enhance the num() on line no 10

# second way to write this code using decorator is 
def decor(num):
    def inner():
        print("If : Before enhancing the function")
        num()
        print("If : After enhancing the fubnction")
    return inner
@decor
def num():
    print("We will use the this function ")
    print("and will enhance this in decorator")
num()
