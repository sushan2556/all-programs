# print fibo using recursion 
def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

no_term = int(input("Enter no of terms that you want to print : "))
for i in range(1, (no_term+1)):
    print(fibo(i))
