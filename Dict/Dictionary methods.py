myDict = {
    "sushant" : "Is a python learner", #sushant is a key with value as Is a python learner
    "learner":"In fast manner" ,# learner is a key with value in fast manner
    "marks" : [10, 20, 30],
    "myDict2" : {'Sushant2':'player'},
    1: 2 #we can keep integer as well
}

# print(myDict.keys()) #prints all keys that are available in the our dictionry
# print(type(myDict.keys())) #prints the type of mydict which is "dict_keys"
# print(list(myDict.keys())) #lists the keys in the dictionary
# print(list(myDict.values())) #you can print the values of the dict as well
# print((myDict.values())) 
# print((myDict.items()))  #will print all the key value contents 
# updateDict = {
#     "lovish" : "friend"
# }
# myDict.update(updateDict) #update function upades the dict with key value 
# print(myDict)
updateDict = {
    "Shweta" : "Wife",
    "learner":"In very fast manner"
}
myDict.update(updateDict)
# print(myDict)
print(myDict.get("sushant2")) #.get method returns none
print(myDict["sushant2"]) #[] brackets return error

