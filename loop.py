# multiplication table

num = int(input("Enter a number for table to print : "))

for i in range(1, 11):
 #   print (str(num) + " X " + str(i) + " =" ,num*i)

# using f string
    print (f"{num}X{i}={num*i}") # type f before string


