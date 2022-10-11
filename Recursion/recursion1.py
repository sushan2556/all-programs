# recursion example 

#factorial example 

# n1 = 1 X 2 X n

# n = 9
# product = 1
# for i in range(n):
#     product = product * (i + 1)
# print(product)

# same programe using function 

# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i + 1)
#     return product
# print(factorial_iter(4))

# recursion example for sum of n natural numbers 

# logic 
# n1 = (n-1)! * n
# sum(n) = sum(n -1 ) + n

# def sumofnatural(n):
#     product = 1
#     for count in range(n):
#         product = product(n-count) + n
#     return product
# print(sumofnatural(4))

# example to see recursion in python 
# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion()

print("######################################33")

# Program to print the fibonacci series upto n_terms

# Recursive function
'''
def recursive_fibonacci(n):
    if n <= 1:
	    return n
    else:
	    return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10

# check if the number of terms is valid
if n_terms <= 0:

    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
for i in range(n_terms):
	print(recursive_fibonacci(i))
'''