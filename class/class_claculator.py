# write a programe to create calculator using class to find square root, square, cube       
class Calculator:
    def __init__(self,num):
        self.number = num
    def square(self):
        print(f"The square of the number {self.number} is {self.number**2}")
    
    def squareRoot(self):
        print(f"The squareRoot of the number {self.number} is {self.number**0.5}")
    
    def cube(self):
        print(f"The cube of the number {self.number} is {self.number**3}")

a = Calculator(3)
a.square()
a.squareRoot()
a.cube()