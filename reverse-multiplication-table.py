num = int(input("Enter a number: "))
for i in reversed(range(1, 11)): # use to print reverse range of the the loop
    # print (str(num) + "X" + str(i) + "=" + str(num*i))
    print (f"{num}X{i}= {num*i}")