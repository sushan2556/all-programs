from os import write


words = ["donkey" , "kaddu", "buddhu"] # list of words that needs to be replaced

with open("sample_file.txt", "r") as f: 
    content = f.read()

for word in words:
    content = content.replace(word, "%^$#@")
    with open ("sample_file.txt", "w") as f:
        f.write(content)
