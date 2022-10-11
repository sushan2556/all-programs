
def decor1(num):
    def inner():
        a = num()
        multi = a*5
        return multi
    return inner

def decor(num):
    def inner():
        b = num()
        add = b+5
        return add
    return inner

def num():
    return 10

num = decor(decor1(num)) # first decor1 will be executed and then decor 
print(num()) 

# other way to write using symbol is 
def decor1(num):
    def inner():
        a = num()
        multi = a*5
        return multi
    return inner
def decor(num):
    def inner():
        b = num()
        add = b+5
        return add
    return inner
@decor1 # this will be executed second
@decor # first this will be executed 
def num():
    return 10
print(num())