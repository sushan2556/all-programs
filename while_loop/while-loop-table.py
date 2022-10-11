#write a prgram to print multiplication table using for loop 

# num = int(input("Enter a even number :"))
# for i in range(1, 11): # range from 1 to 11, start to stop
    #print(str(num) + "X" + str(i) + "=" + str(i*num)) #string concatinated
    #Other way 
    # print(f"{num}X{i}={i*num}") # using f string

#write a prgram to print multiplication table using for while loop
 
num = int(input("Enter a even number :"))
count = 0

while count <11:
    print(str(num)+" X "+str(count)+" = "+str(num*count))
    count=count + 1