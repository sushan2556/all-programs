# with statement in python 

with open("another_file.txt", "r") as f:
    a = f.read()

with open("another_file.txt", "w") as f:
    a = f.write("me")

print(a)
# the best way to open and automatically close the file is with statement 
# no need to write f.close in the above example as write function closes the file

a = 10
b = 2
print(a)