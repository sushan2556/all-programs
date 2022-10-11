# make a copy of file

with open ('this.txt', 'r') as f:
    content = f.read()

with open ('copy-of-this.txt' , 'w') as f:
    f.write(content)