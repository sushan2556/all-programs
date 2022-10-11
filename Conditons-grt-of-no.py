'''find the greates no entered ny user'''
'''
a = int(input("Enter first no :"))
b = int(input("Enter second no :"))
c = int(input("Enter third no :"))
d = int(input("Enter fourth no :"))
if (a>b and a>c and a>d):
    print("a is the greatest no ")
elif(b>a and b>c and b>d):
    print("b is the greatest no")
elif(c>a and c>b and c>d):
    print("C is the greatest no")
else:
    print("d is the greatest no")
'''
#another way of writing the program 

num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
num3 = int(input("Enter number 3 :"))
num4 = int(input("Enter number 4 :"))

if(num1>num4):
    f1 = num1
else:
    f1 = num4

if (num2>num3):
    f2 = num2
else:
    f2 = num3

if (f1>f2):
    print(str(f1)  + " Is the gretest no") #coverting f1 into str to add the later str to it
else:
    print(str(f2) + " is the greatest no")