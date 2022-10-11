# find the factorial of num
# n = n*3*2*1
# base condition is n == 1
def facto(n):
    if n==1:
        return 1
    else :
        return n * facto(n-1)

n = int(input("Enter no :"))
print(facto(n))
