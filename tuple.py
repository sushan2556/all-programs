# tuple is read only version of list

#immutable
t=(1,2,3)
print(t[0])

# t[0]=4 # item assignment is not possible hence tuple is immutable 
# print(t[0]) 

#indexing and slicing is possible in tuple 
t=(1,2,3,4)
#indexing
print(t[0])
#slicing
print(t[0:2])
