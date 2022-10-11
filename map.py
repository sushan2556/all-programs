# map.py

def square(num):
    return num*num

l = [1, 2, 3]
# Method 1

l2 = []
for item in l:
    l2.append(square(item))
print(l2)

# second function using map

print(list(map(square, l))) # typecasting it to list, map(function, iterables) --> map objects

# map applies to all the intems in the item list
#Syntax :
# map(function, input_list) --> function can be lambda function