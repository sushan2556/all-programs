a = 54 #global variable
def func1():
    global a
    print(f"Print statement 1 = {a}") # this will print the global value of a
    a=8 # local variable
    print(f"Print statement 2 = {a}") # this has changed the local value of a from 54 to 8

func1()
print(f"Print statement 3 = {a}")  # this will again oprint the changed global value 