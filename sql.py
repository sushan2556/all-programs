import mysql.connector as c
con=c.connect (host='localhost',user='Root12',passwd='Root12!@', database='cricket')
if con.is_connected():
    print("Successfully connected..")
else:
    print("Not successfull..")
