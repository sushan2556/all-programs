# write a programe to find if the given number is prime or not

num = int(input("Enter a number : ")) # num interger taken from user
prime = True # initially the conditon is set to true

for count in range (2, num): # for loop with range function , start(2) , end (num)
    if (num%count == 0):
        prime = False
        break
if prime:
    print ("The number entered is prime ")
else:
    print ("The number entered is not prime")
