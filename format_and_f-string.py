# format method and fstring in python
# template --> format (p1, p2) positional argument

name = "Sushant"
a = f"this is {name}"
print(a)

#using format in python

name = "Shweta"
type = "female"
caste = "Hindu"
s = "this is {}".format(name) # using format method
r = "this is {0} and she is {1} and her caste is {2}".format(name,type, caste) # format (argument1, argument2). from index zero
print(r)

# template first and arguments in curly brackets 
