#Dictionary creates multiple key and value elements
#Dictionary is indexed , triggering key it shows up the value
myDict = {
    "Sushant" : "Is a python learner", #Sushant is a key with value as Is a python learner
    "Learner":"In fast manner" ,# learner is a key with value in fast manner
    "Marks" : [10, 20, 30],
    "myDict2" : {'Sushant2':'player'}
}

# print(myDict["Sushant"]) #printing key element which returns the value 
# print(myDict["Learner"]) #
# print(myDict["Marks"])
print(myDict['myDict2']['Sushant2'])
#Dictionary uses curly brackets 
#Does not contains order
#Dictionary is mutable
# myDict["Marks"]= [40,50,60]
# print(myDict["Marks"])

