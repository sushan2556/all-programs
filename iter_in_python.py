# iterator and next method in python 

my_list = [14,22,63,94,35]

# define a iterator 
my_iter = iter(my_list) # iter keyword is used to create and iterator containing iterable object 

#iterate through the list using next()

print(next(my_iter)) # output - first element 14 
print(next(my_iter)) # output - second element 22
print(next(my_iter)) # output - third element 63
print(next(my_iter)) # output - fourth element 94
# next()keyword is used to call the next element in the iterable object , here it is list

print("######")
print(my_iter.__next__()) # output - fifth element 35
print(my_iter.__next__()) # throws error - StopIteration
print(next(my_iter)) # throws error - StopIteration
