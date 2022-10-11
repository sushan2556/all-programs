try:
    i = int(input("enter a number: "))
    c = 1/5
except Exception as e:
    print(e)

else:
    print("we were successfull") # this will be executed only when try was successfull

