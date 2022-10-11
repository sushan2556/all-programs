# DRy principle , means do not repeat yourself 

class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"name is {self.name}")
        print(f"train name is {self.train}")

sushantApplication = RailwayForm() # new form is created for my instance .. New instance is created 
sushantApplication.name = "Sushant" #name has been set
sushantApplication.train = "Rajdhani Express" # train name has been set
sushantApplication.printData() # print function called

shwetaApplication = RailwayForm() # new form is created for my instance .. New instance is created 
shwetaApplication.name = "Shweta" #name has been set
shwetaApplication.train = "Gareeb Rath" # train name has been set
shwetaApplication.printData() # print function called

# abstraction - no need to do details 

#encapsulation - wrapping all the function in one entity 
# all methods added in one class 