'''import mysql.connector
import pymysql  

my_conn=pymysql.connect(
        host='localhost',
        user='Root12', 
        password = 'Root12!@',
        db='cricket',
        )

my_cursor = my_conn.cursor()
my_cursor.execute("SELECT * FROM cricket_team")
my_result = my_cursor.fetchall() # we get a tuple
# print(my_result)

# print(dir(pymysql))
print(dir(mysql.connector))
'''

import pymysql
#Create the connection object   
myconn = pymysql.connect(
    host = "localhost", 
    user = "Root12",
    passwd = "Root12!@",
    database = "cricket"
)  
#printing the connection object   
print(myconn)
#creating the cursor object  
cur = myconn.cursor()
cur.execute('select * from cricket_team')