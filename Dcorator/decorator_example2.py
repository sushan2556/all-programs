#I have enhance the num function to return 15
def decor(num):
    def inner():
        a = num() # this fun will have num , this will go to line no 9
        add = a+5
        return add
    return inner
 
def num():
    return 10
num = decor(num) # first this will be executed , which will call the decor function in which num will be passed .
                        # inner function will be stored in result_fun, result_fun is function variable 
print(num()) # inner fun will be called over here, variable with parenthesis means function is called
                    # this will go to line no 3

# the purpose is to enhance the main function which is num() over here. It is providing 10 I want 15 out of it 

# second way to write using @ symbol is 
def decor(num):
    def inner():
        a = num() # this fun will have num , this will go to line no 9
        add = a+5
        return add
    return inner
@decor 
def num():
    return 10 
print(num())