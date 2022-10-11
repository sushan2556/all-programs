# write a file to add peom and find twinkle word 

f = open("peom.txt") # default it is opened in read mode
t = f.read() # read data will be stored in t variable
if 'diamond' and 'little' in t: # find word twinkle in t , can use logical operators as well
    print("Yes")
else:
    print("No")
f.close() # close the file

