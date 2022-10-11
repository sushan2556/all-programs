
'''
print the below pattern using for loop
  *
 ***
*****

'''
'''
n = 3 
for count in range(3):
    print (" " * (n-count-1), end="")
    print ("*" * (2*count+1), end="")
    print (" " * (n-count-1)),
'''

n = 3
for count in range (3):
    print(" " * (n-count-1), end=""),
    print("*" * (2*count+1), end=""),
    print(" " * (n-count-1), )
    