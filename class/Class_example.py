# create a class prpogramer to store info for emplyee in microsoft

class  Programer:
    company = "Microsoft" # company over here is class attribute

    def __init__(self, name, product):
        self.name= name
        self.product = product
    def getinfo(self):
        print (f"The name of the programer is {self.name} in company {self.company} and the product is {self.product}")


sushant = Programer("Sushant", "Windows")
shweta = Programer("Shweta", "Windows")
sushant.getinfo()
shweta.getinfo()
