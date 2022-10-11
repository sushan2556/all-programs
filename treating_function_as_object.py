# Treating a function as an object in Python 
def shout(text):
    return text.upper()

print(shout("Hello"))
yell = shout # function has been assinged to yell object
print(yell("Hello"))

# Passing the function as an argument 
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("hi, how are you ?")
    print(greeting)

greet(shout)
greet(whisper)

# # Returning function from another function 
# def create_adder(x):
#     def adder(y):
#         return x+y
#     return adder

# add_15=create_adder(15)
# print(add_15(10))

