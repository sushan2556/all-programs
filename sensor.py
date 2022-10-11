# write a propgram that will sensor the word in another file with ######

from os import replace
words = ["Donkey", "Mad", "ass"]

with open ("sample.txt", "r") as f:
    content = f.read() # file content is stored in content variable

for word in words:
    content = content.replace(word, "@#$%^&") # replace function used to replace the donkey work with sensor

with open ("sample.txt", "w") as f:
    f.write(content) #write function used to replace the words 

