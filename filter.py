# filter 

def greaten_than_5(num):
    if num>5:
        return True
    else:
        return False
g10 = lambda num: num>10
l = [1,2,3,4,5,6,7,8,9, 13,15]
# print(list(filter(greaten_than_5, l))) # this will print all the values that are greater than 5 in the list
print(list(filter(g10, l)))

# Syntax - print(list(filter(function, list)))