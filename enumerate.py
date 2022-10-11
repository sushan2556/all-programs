# use of innumerate function in python 

list1 = [10, 3.2, "Sushant", False,]

# print(list1) # to print items in the list

'''
index = 0 # this will print the index values of the items in the list
for item in list1:
    print(item, index)
    index += 1
'''

# using innumerate 
for index , item in enumerate(list1): # it always has to be index first and item second
    print(item, index) # this can be anyhow

# and Emumarate function adds counter to an iterable and returns it