# Recursion topic 
'''
def demo1():
    ------------
    -----------
    demo()

def demo2():
    ------
    ------
    demo1()


'''

# Sum of natural numbers using recursion 
# 4 = 4+3+2+1
def Sum(n):
    if n==1:
        return 1
    else: 
        return n + Sum(n-1)

n = int(input("Enter no :"))
print(Sum(n))

''''
n = 4 

4+ sum(3) = 10
3 + sum(2) = 6
2 + sum(1) = 1

'''

