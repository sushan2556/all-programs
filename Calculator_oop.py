# write a class calculator capable of finding square , cube and squareroot of a number

class Calculator():
    def __init__(self, num): # constructor created which will run automatically
        self.number = num # variable created to store the value
    
    def square(self): #function/method created 
        print(f"The square of {self.number} is {self.number **2}")

    def squareroot(self): #function/method created 
        print(f"The squareroot of {self.number} is {self.number **0.5}")

    def cube(self): #function/method created 
        print(f"The cube of {self.number} is {self.number **3}")

a = Calculator(3) # created and instance for calculator class and pass parameter as 3
a.square() # Call method
a.squareroot() # Call method
a.cube() # Call method