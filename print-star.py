# Writre a prgrame to print following star pattern
'''
*
**
***

'''

# count = 3

# for i in range (3):
    # print("*" * (i+1) )


# print the following pattern 
'''
    *   
  * * *   
* * * * *
'''

n = 3
for i in range (3):
    print(" " * (n-1-1), end="")
    print("*" * (2*1+1), end="")
    print(" " * (n-1-1))