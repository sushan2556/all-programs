# pragrame to detect if the text entered is a spam text or not 

text = input("Enter your text \n")

if("make a lot money" in text):
    spam = True
elif("Subscribe" in text):
    spam = True
elif("watch this" in text):
    spam = True
elif("buy now" in text):
    spam=True
else:
    spam = False

if(spam):
    print("this is a spam text")
else:
    print("This is not a spam text")