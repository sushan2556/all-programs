# list comprehension is an elegant way to create list based on existing list

a = [12, 13, 15, 2, 23, 122]

b = []
for item in a:
    if item%2==0:
        b.append(item)

print(b)

#using list comprehansion 

b = [i for i in a if i%2==0]
print(b)

# this can be used in set as well as dictionary 