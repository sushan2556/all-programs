# change the self parameter in class 

class Sample:
    def __init__(self, name):
        self.name = "Sushant"
    
obj = Sample("self.name")
print(obj.name)