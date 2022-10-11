#maximum of list
from functools import reduce

l = [1, 2, 3, 5,78, 89, 123, 563]

# print(max(7,9)) --> max is the function in python 

a = reduce(max, l) 
print(a)
