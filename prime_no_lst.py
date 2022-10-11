# Find the prime number from the list

lst = [7,2,3,4,5,6,7,87,9] # list is defined 
l = len(lst) # length of list is set to a variable 
for i in range(0,l): # index from 0 to lenght of list
    # first element in the range is 7
    c = 0 # one condition is set initially
    for j in range(2,lst[i]):
        # j in range of first element ie 7, so range is 2,3,4,5,6
        if lst[i]%j==0:
            # if 7 % j(2) == 0
            c=1
            # for 7 , the above condition is not true, so c stays as 0
            break
    if c ==0:
        print(lst[i]," is a prime number")
    else:
        print(lst[i]," is not a prime number")