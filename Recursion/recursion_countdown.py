# countdown to zero using recursion 
def count_down(num):
    print(num)
    # recursive function should have a base condition
    if num == 0:
        return
    else:
        count_down(num - 1) # function calls itself over here

num = int(input("Enter the number :- "))
print(count_down(num))

# more consise way to express this 
def count_down(num):
    print(num)
    if num > 0:
        count_down (num-1)


num = int(input("Enter the number :- "))
print(count_down(num))
