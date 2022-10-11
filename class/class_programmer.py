# create a class programmer for storing information of few programmer working at microsoft

class Programer():
    # microsoft is common for both employee , so attribute is set in the class
    company = "Microsoft"

    def __init__(self, name, product):  # contructor created with argument name and product
        self.name = name  # instance created
        self.product = product

    def getInfo(self):
        print(
            f"The name of the developer is {self.name} and the product is {self.product} in company {self.company}")


# object created with attributes name and product
Sushant = Programer("Sushant", "youtube")
Shweta = Programer("Shweta", "Tiktok")
Sushant.getInfo()
Shweta.getInfo()
