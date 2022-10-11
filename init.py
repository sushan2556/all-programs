# overwrite Parent class init Method using Child class


class Parent:
    def __init__(self, fname, fage):
        self.name = fname
        self.age = fage
    def View(self):
        print(self.name, self.age)
    
class Child:
    def __init__(self, fname, fage):
        Parent.__init__(self,fname,fage) # calling parent class contructor 
        self.lastname = "Jadhav"
    def View(self):
        print(self.age, self.lastname, self.name)

ob = Child("Sushant",34)
ob.View()

# Types of inheritance 
# Single inheritance --> One parent one child 
print("######### Single -->########")

class Parent:
    def func1(self):
        print("This is function one")

class Child(Parent):
    def func2(self):
        print("This is func two")

ob = Child()
ob.func1() # inheritates the Parent function , single inheritance  

print("######### Multiple -->########")
class Parent:
    def func1(self):
        print("This is function one")

class Parent2:
    def func3(self):
        print("This is function three")

class Child(Parent,Parent2):
    def func2(self):
        print("This is func two")

ob1 = Child()
ob1.func3()

print("######### Multilevel inheritance -->########")

class grand_Parent:
    def func1(self):
        print("This is function one")

class Parent2(grand_Parent):
    def func3(self):
        print("This is function three")

class Child(Parent2):
    def func2(self):
        print("This is func two")

ob1 = Child()
ob1.func1()

print("######### hierarchical inheritance -->########")

class Parent3:
    def func1(self):
        print("This is function one")

class Child1(Parent3):
    def func3(self):
        print("This is function three")

class Child2(Parent3):
    def func2(self):
        print("This is func two")

ob4 = Child2()
ob4.func1()
ob5= Child1()
ob5.func1()

print("######### Hybrid inheritance -->########")

class Parent:
    def func1(self):
        print("This is function one")

class Parent2(Parent):
    def func3(self):
        print("This is function three")

class Parent3():
    def func3(self):
        print("This is function three")

class Child5(Parent,Parent3):
    def func2(self):
        print("This is func two")

ob5 = Child5()
ob5.func1()

print("########### Super function ###########")

class Parent5:
    def func6(self):
        print("This is func6 of Parent5 class")

class Child6(Parent5):
    def func7(self):
        super().func6() # super function is use to call the parent method directly
        print("This is the child7 function")

ob6 = Child6()
ob6.func7()

print("########## Method overriding ###############")

class Parent6:
    def func8(self):
        print("This is func8 Original")

class Child7(Parent6):
    def func8(self): # Method overriding 
        print("This is func8 overriden")

ob7 = Child7()
ob7.func8()