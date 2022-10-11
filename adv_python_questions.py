# write a progame to open 3 files , 1.txt, 2.txt and 3.txt If any of this files are not present a message without exiting the
# programe must be printed with the same 

def readFile(filename):
    try:
        with open (filename, "r") as f:
            print(f.read())
    except FileNotFoundError: # if any file is deleted the filenotfound exception will continue the program 
        print(f"the file {filename} is not there")

readFile("1.txt")
readFile("2.txt") 
readFile("3.txt")

# after deleting 2.txt file we will use the exception handling with try function 
