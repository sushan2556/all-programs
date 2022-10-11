# write a programe to calculate the factorial of a given number
# !n = 1 X 2 X 3 X 4 X 5 X 6 x n
# !5 = 1x2x5x4x5

# num = int(input("Enter a number : ")) 
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i
# print(f"The factorial of {num} is {factorial}")

def factorial_of_num(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i
    print(f"the factorial of {num} is {factorial}")

factorial_of_num(6)