'''
decorator is a function which takes  a functyion as argument  and  extend its functinality and return
mofified function with extended functinality.
'''

'''
def decor(func):
    def inner(name):
        if name=='lalit':
            print('hello',name,'bad morning')
        else:
            func(name)
    return inner        

@decor
def wish(name):
    print('hello',name,'good morning')
# wish('sakshi')    
wish('lalit')

#############################################################
print('#######################################################')
def smart_div(func):
    def inner(a,b):
        print(f'we are dividing {a} and {b} ')
        if b==0:
            print('oops we can not divide')
        else:
            return func(a,b)    
    return inner  
@smart_div          
def division(a,b):
    return a/b
    
print(division(20,3))
print(division(20,3))
'''
##############################################################################
#decorator chaining
print('#######################################################')
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
#############################################################################