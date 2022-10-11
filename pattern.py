# printing different pattern in python
# we can use the matrix of 5X5 
'''
11 12 13 14 15
21 22 23 24 25
31 32 33 34 35
41 42 43 44 45
51 52 53 54 55
'''
# print pattern c 

for i in range(1,6):
    for j in range(1,6):
        if j==1 or i==1 or j ==5:
            print('*',end="")
        else:
            print(" ",end="")
    print("")

# print pattern N
for i in range (1,6):
    for j in range (1,6):
        if j==1 or j==5 or i==j:
            print("* ",end="")
        else:
            print("",end="")
    print("")