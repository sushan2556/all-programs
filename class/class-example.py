class Phone: #class defined here 
    def make_Call(self): #method 1 of the class 
        print("I am making a call")
    def play_Game(self): # method 2 of the class 
        print("I am playing a Game")
    
p1 = Phone() # created object of the class , reference variable or instance of class 
p1.make_Call()
p1.play_Game()

class Phone:
    def set_color(self,color): # object features   / seting parameters 
        self.color = color
    def set_cost(self,cost): # object features
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    
p1 = Phone()
p1.set_color("Red")
p1.set_cost(10000) 
print(p1.show_color())
print(p1.show_cost())

# second example using contructed to pass value while creation of object

class Employee:
    def __init__(self,name, age, salary, gender): #first method to take parameter
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
    
    def show_emp_details(self): # 2nd method to show details
        print(f"Name of emplyee is {self.name}")
        print(f"Name of emplyee is {self.age}")
        print(f"Name of emplyee is {self.salary}")
        print(f"Name of emplyee is {self.gender}")

e1 = Employee("Sushant",32,100000,"Male") # object instantiate , E1 is instance 
print(e1.show_emp_details()) # show emp details method invoked here 
print("################# inheritance in oops ################")
# inheritance in OOPS

class Vehicle(): # parent class , base class, super class
    def __init__(self,milage, cost):
        self.milage = milage
        self.cost = cost
    
    def Show_vehicle_details(self):
        print(f"Milage of vehicles is {self.milage}")
        print(f"Milage of vehicles is {self.cost}")
        print("I am a vehicle")
    
v1 = Vehicle(80, 100000)
print(v1.Show_vehicle_details())

class Car(Vehicle): # child class isinheriting properties from super class (Vehicle)
    def show_car_detail(self):
        print("I am a car")

c1 = Car(300, 202350)
print(c1.Show_vehicle_details()) # child class showing methods of parent class 
print(c1.show_car_detail())

print("############ override __init__ method ################")
print("############## creating constructor in child class #############")
print("######### using super method , super class########### ")
print("########## Single Inheritance ################")

class Vehicle(): # parent class , base class, super class
    def __init__(self,milage, cost):
        self.milage = milage
        self.cost = cost
    
    def Show_vehicle_details(self):
        print(f"Milage of vehicles is {self.milage}")
        print(f"Milage of vehicles is {self.cost}")
        print("I am a vehicle")

v1 = Vehicle(80, 100000)
class Car(Vehicle): # child class , where init method is overriding te init method or parent class
    def __init__(self,milage, cost, tyre, hp):
        super().__init__(milage,cost)
        self.tyre = tyre
        self.hp = hp
    def Show_car_details(self):
        print(f"No of tyres in car {self.tyre}")
        print(f"No of tyres in car {self.hp}")
        print("I am a car")

c1 = Car(600,10000,4,120)
print(c1.Show_car_details())
print(c1.Show_vehicle_details())

print("###################multiple inheritance #############")
print("################## Two Parents one child ###########")

class Parent1():
    def assign_str_one(self,str1):
        self.str1 = str1
    def show_assign_str1(self):
        return self.str1

class Parent2():
    def assign_str_two(self,str2):
        self.str2 = str2
    def show_assign_str2(self):
        return self.str2
    
class Child(Parent1, Parent2):
    def assign_str_three(self,str3):
        self.str3 = str3
    def show_assign_str3(self):
        return self.str3
my_Child = Child()
my_Child.assign_str_one("i am string of parent One")
my_Child.assign_str_two("i am string of parent two")
my_Child.assign_str_three("i am string of parent three")
print(my_Child.show_assign_str1())
print(my_Child.show_assign_str2())
print(my_Child.show_assign_str3())

print("################ Multilevel Ineritance ##############")
print(" ############ Parent --> Child --> Grand child #######")

class Parent_main():
    def assign_str_parent(self,parent):
        self.parent = parent
    def show_assign_parent(self):
        return self.parent
    
class Child_main(Parent_main):
    def assign_str_child(self,child):
        self.child = child
    def show_assign_child(self):
        return self.child

class Grand_child(Child_main):
    def assign_str_grandchild(self,grandchild):
        self.grandchild = grandchild
    def show_assign_grandchild(self):
        return self.grandchild

gc = Grand_child()
gc.assign_str_parent("DAD")
gc.assign_str_child("SON")
gc.assign_str_grandchild("Nephew")
print(gc.show_assign_parent())