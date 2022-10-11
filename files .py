# files .py 

# from os import close
# use open function to read file in python

# f = open("sample.txt", "r") # f means calling file function , open("filename", "mode") 
# data = f.read()  # data is variable here with read function
# print(data) 
# f.close # closing the file

# readline function in python 

# readline function in python , readline function will read lines in the txt file

f = open("D:\June-11\Programs\sample.txt", "r")
for each in f:
    print(each)

f = open("D:\June-11\Programs\sample.txt", "r")
print(f.read())

f = open("D:\June-11\Programs\sample.txt", "r")
print(f.read(3)) # read mode character wise 

print("############# Python code to create a file ############")
file = open("test1.txt", "w")
file.write("This is the first line of code")
file.write("This is the second line of code")
file.close() # close command terminates all the resources in use and frees up the system

print("##############3 Working on append Mode #############")
file = open("test1.txt","a")
file.write("This is the appended code")
file.write("This is also the added code")
file.close()

# print("############## Python code to illustrate with() #############")
# with open ("test1.txt","a") as f:
#     f.write("This is using with")
#     data = f.read()
# print(data)

print("################## working with csv file ##################")
import csv

#field names in the csv file
fields = ['name','Branch','Address','fees']

# data rows of csv files
rows = ['Sushant','Pimpri','pune',20000]

#name of the csv file to be created
filename = "student_record.csv"

with open (filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile) # creating a csv writer object
    csvwriter.writerow(fields) # writing fields 
    csvwriter.writerow(rows) # writing rows

print("########## using split in file handling ###########")
with open("test1.txt","r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

