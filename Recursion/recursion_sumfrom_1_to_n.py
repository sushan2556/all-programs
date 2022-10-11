# print the sum from 1 to n using recursion 
# n is from user, suppose n is 10 so 10+9+8+7+6+5+4+3+2+1


def sum_of_num(n):
    if n == 1:
        return n
    else:
        return n + sum_of_num(n-1)

n = int(input("enter number to calculate sum :- "))
print(sum_of_num(n))