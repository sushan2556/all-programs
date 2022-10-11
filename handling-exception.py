# handling exception in Python

try:
    a=int(input("Enter a number "))
    c = 1/a
    print(c)
except ZeroDivisionError as e: # handling zero division error 
    print("Please do not enter 0")

except ValueError as e: # handling incorrect value error 
    print("Enter correct value")

print("Thank you for using this code")