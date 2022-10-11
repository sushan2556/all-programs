#creating a dictionarty with hindi words(Key) and english meaning (values)
myDict = {

    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}
print("Options are : ", myDict.keys())
a = input("Enter a Hindi Work : \n")
print("The meaning of your word is :", (myDict[a]))