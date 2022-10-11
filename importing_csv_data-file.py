import pymysql
import pandas as pd

# importing csv file using pandas framework read oject created as data
data = pd.read_csv (r'C:\Users\RSC\Downloads\Resource_Adhrence.csv')

#creating dataframe object of read object
df = pd.DataFrame(data)
print(df)

mydb = pymysql.connect(
    host='localhost',
    user='Root12',
    passwd='Root12!@'
)
mycursor = mydb.cursor()
'''
#once created you do not have to create again 
mycursor.execute('Create database Adherance')
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
'''

mycursor.execute("USE Adherance")
#creating table, once created do not have to execute again 
# mycursor.execute("CREATE TABLE emp_adherance (proc_name VARCHAR(100), emp_name VARCHAR(100), adhe_perc INT(100))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

#inserting dataframe to emp_adherance table
for row in df.itertuples():
    mycursor.execute('''
                    INSERT INTO emp_adherance (proc_name, emp_name, adhe_perc)
                    VALUES (?,?,?)
                    ''',
                    row.proc_name, 
                    row.emp_name,
                    row.adhe_perc
                    )
mydb.commit()