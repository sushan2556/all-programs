# reduce functionality of python 

from functools import reduce # import reduce function before programe
sum = lambda a, b: a+b 
l = [1,2,3,4,5,]
val = reduce(sum,l)
print(val)

# reduce applies rolling computation to sequencial pair of elements 
