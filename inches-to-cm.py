# write a programe to convert inches to cm
# multiply the length value by 2.54

n = int(input("Enter inches to be converted to cm : "))

def inctocm(n):
    return n * 2.54

print("Value in cm is : ", inctocm(n))
