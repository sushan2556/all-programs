#creating a dictionarty with hindi words(Key) and english meaning (values)
myDict = {

    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}
print("Options are : ", myDict.keys()) ,#mydict.keys displays all the keys that are available in dictionary
a = input("Enter a Hindi Word : \n")
# print("The meaning of your word is :", (myDict[a])) #this will show the values , but entered invalid key will give a error
print("The meaning of your word is: ", myDict.get(a)) #get function will return value as none if key is not present in the dict