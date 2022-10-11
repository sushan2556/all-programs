# OOP by railway example 

class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train name is {self.train}")

SushantApplication = RailwayForm()
SushantApplication.name = "Sushant"
SushantApplication.train = "Local"
SushantApplication.printData()