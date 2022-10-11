# prime number is divisible by itself and 1

num = int(input("Enter a number : "))
prime = True
for count in range (2, num):
    if num%count == 0:
        prime = False
        break

if prime :
    print ("The number is prime number ")
else:
    print("The number is not prime")
