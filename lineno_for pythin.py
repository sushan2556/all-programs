# print out the line no in swhich pythin is present

with open ("log.txt") as f:
    content = f.readline()

if 'python' in content.lower(): #find python in content file in lower case
    print("yes, python is present")
else:
    print("pythin is not present")
