'''
generator is a function which is responsible to generate sequence of value..
'''
def mygen():
    # yield 'B'    #genertor object
    # yield 'c' 
    for i in range(10):
        yield i
g=mygen()
print(type(g))    
print(next(g))   #print single value at a time
print(next(g))
print(next(g))   #print single value at a time
print(next(g))
print(next(g))   #print single value at a time
print(next(g))
print(next(g))   #print single value at a time
print(next(g))
print(next(g))   #print single value at a time
print(next(g))
print(next(g))   #print single value at a time
print(next(g))


#iter and next method
#iterable/ iterator
#sequence and collection