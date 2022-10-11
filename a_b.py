# write a program to print a/b value as integer 
# also, handle error zero divisional error

a = int(input("Enter number a :"))
b = int(input("Enter number b :"))

try:
    print(a/b)
except:
    print("infinite")
