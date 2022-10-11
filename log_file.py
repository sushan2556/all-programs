# print out if python is present or not

with open ("log.txt") as f:
    content = f.read()

if 'python' in content.lower(): #find python in content file in lower case
    print("yes, python is present")
else:
    print("pythin is not present")

