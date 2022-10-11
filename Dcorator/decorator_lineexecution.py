def sqr(func):
    def inner():
        x=func()
        return x*x
    return inner    
def decor(func):
    def inner():
        x=func()
        return 2*x
    return inner
@decor
@sqr
def num():
    return 3
print(num())