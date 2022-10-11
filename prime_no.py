# Find the prime number from the list

lst = [1,2,3,4,5,6,7,87,9]
l = len(lst)
for i in range(0,l):
    c = 0
    for j in range(2,lst[i]):
        if lst[i]%j==0:
            c=1
            break
    if c ==0:
        print(lst[i]," is a prime number")
    else:
        print(lst[i]," is not a prime number")