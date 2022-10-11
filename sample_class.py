# create a class with class attribute a, create and object from it and set a directly using object a = 0
# will this change the class attribute? No, it doesn't

class Sample:
    a = "Sushant" # this is class atribute 

obj = Sample()
obj.a = "Shweta" # new instance attribute is set 
# Sample.a = "Shweta" # this will change the class attribute

print(Sample.a)
print(obj.a)