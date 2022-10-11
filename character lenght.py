#program to identify the lenght of the usenname entered 
username = input("Enter your username : ")
lenght = len(username) #len function counts the lenght of the str
if (lenght<5 or lenght==10): 
    print("Username should be atleasr 10 chara")
else:
    print("username is more than 10 char")
