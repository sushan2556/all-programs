# create a class class attribute and instance attribute and see if it changes the class attribute

class Sample:
    a = "Sushant" # class attribute is set
    # this a is an class attribute 

obj = Sample() # object created 
obj.a = "Shweta" # instance attribute is created with this 
        # this a is an instance attribute 
        
print(obj.a) # this will print the instance attribute first and than class attribute
print(Sample.a) # this will print the class attribute 

