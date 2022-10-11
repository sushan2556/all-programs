# write a python function to write multiplication table

# num = int(input("Enter a even number:  "))
# for i in range(1, 11):
#     # print(str(num) + "X" + str(i) + "=" + str(i*num)) # str concatinate 
#     print(f"{num}X{i}={num*i}") # using f string

def multiplication_table(num):
    return (str(num) + "X" + str(i) + "=" + str(i*num))

num = int(input("Enter a number :"))
for i in range (1, 11):
    print(multiplication_table(num))


