# connecting to mysql database 
import pymysql
# import numpy
import matplotlib.pyplot as plt

#creating object of my database 
mydb = pymysql.connect(host='localhost',
                       user='Root12',
                       passwd='Root12!@',
                       database='employee_details'
                       )

#Creating cursor object - It is an object that is used to make the connection for executing SQL queries
mycursor = mydb.cursor()

#fetching data from database using cursor object 
mycursor.execute("Select emp_name, emp_phno from emp_details")
result = mycursor.fetchall

Names = []
phno = []

for i in mycursor:
    Names.append(i[0])
    phno.append(i[1])

print(f'Names of employee {Names}')
print(f'Phno of employee {phno}')

#visualising the data using matplotlibs 
plt.bar(Names,phno)
plt.ylim(80,680)
plt.xlabel("Names of employee")
plt.ylabel("Phno of employee")
plt.title("Employee_Name"+Names)
plt.show()