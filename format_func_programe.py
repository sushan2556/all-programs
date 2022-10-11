# write a programe to input name marks and phone number of a student and format it using the format function like below 

# the name of student is Sushant and his marks are 72 and his phone number is 9860653218

name = input("Enter the name of the student : ") 
marks = int(input("Enter the marks of the student : "))
phonenum = input("Enter the phone number of the student ")

str = "The name of the student is {} and his marks are {} and his phone number is {}".format(name,marks,phonenum)
print(str)
