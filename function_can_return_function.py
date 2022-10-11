

def create_adder(x): #create added function returns adder function 
    def adder(y):
        return x+y
  
    return adder
  
add_15 = create_adder(15) #15 will go as x
  
print (add_15(10)) #10 will go as y

############# second example passing a function to another function ############

def do_twice(func):
  func()
  func()

def say_hello():
  print("Hello!")

do_twice(say_hello)

################# return a function from another function ############

def return_to_upper():
  return str.upper

to_upper = return_to_upper()

print(to_upper("scaler topics"))

############# inner function ###############
def parent():
  print("I am the parent function")

  def first_child():
    print("I am the first child function")

  def second_child():
    print("I am the second child function")

  first_child()
  second_child()

parent()

############## Closure (inner function can access variable in the outer scope of the enclosing function) ################

def outer(message):
  def inner():
    print("Message:", message)

  return inner

hello_msg = outer("Hello!")
hello_msg()

bye_msg = outer("Bye!")
bye_msg()