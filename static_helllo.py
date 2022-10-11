# static program to greet hello

class Calculator:
    def __init__(self,num):
        self.number = num
    def square(self):
        print(f"The square of the number {self.number} is {self.number**2}")
    
    def squareRoot(self):
        print(f"The squareRoot of the number {self.number} is {self.number**0.5}")
    
    def cube(self):
        print(f"The cube of the number {self.number} is {self.number**3}")
    
    @staticmethod
    def greet():
        print("********Welcome to the best calculator in the world********")

a = Calculator(3)
a.greet()
a.square()
a.squareRoot()
a.cube()