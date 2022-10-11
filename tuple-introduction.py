#tuple does not allow value assignment
# tuple = (1,2,3,4) #round brackets describe tuple , square bracket describe list
# # tuple[0]=2
# print(tuple)

#blank tuple
s = ()
print(type(s))

s1 = (1,2,3)
print(min(s1)) # find minimum 
print(max(s1)) # find max of numbers
s2 = (4,5,6)
print(s1+s2) # we can concatinate tuple but not any int value with tuple ie t1 + 2
print(s1.count(3)) # count method to count elements in the tuple

t=(1,2,3,4,5)
r=t
print(id(t))
print(r)

#Methods in tuple
'''
Sorting , finding min and maximum 
count()



''' 