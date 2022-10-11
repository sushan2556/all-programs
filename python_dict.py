mydict = {
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "chappel" : "Sandals"
}
print ("The values in the dictionary are :" , mydict.keys()) #this will print all the keys in the dictionary
a = input("enter the key ")
# print("the value of the key entered is :" , mydict[a]) #mydict[a] will through error if entered wrong key
print("the value of the key entered is :" , mydict.get(a)) #.get function does not throw error 