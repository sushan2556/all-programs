# programe to write a multiplication table for even number
# num = int(input("Enter a even number:  "))
# for i in range(1, 11):
#     # print(str(num) + "X" + str(i) + "=" + str(i*num)) # str concatinate 
#     print(f"{num}X{i}={num*i}") # using f string



# # same program with while loop
# num = int(input("Enter a even number:  "))

# while 

num = 10
print(type(num))
for n in range(1, 11):
    # print (f"{num} X {n} = {num*n}")
    print(str(num) + "X" + str(n) + "=" + str(n*num)) # str concatinate 

n=1
while n < 11:
    for n in range(1,11):
        print (f"{num} X {n} = {num*n}")
        n+=1