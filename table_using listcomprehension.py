# write a list comprehansion to print a list which contains the multiplication table of a user entered number

num = int(input("Please enter a number : "))

table = [num*i for i in range(1, 11)] # list comprehension 
print(table)

# list comprehension is an elegant way to create list based on existing list
