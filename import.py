import pymysql
import pandas as pd

# importing csv file using pandas framwork read oject created as data
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
mycursor.execute('Create database movies_details')

CREATE TABLE movies_details(
                               star_rating float(2,1),
                               title varchar2(100),
                               content_rating varchar2(10),
                               ……);

# creating column list for insertion 
cols = “,”.join([str(i) for i in data.columns.tolist()])

# Insert DataFrame records one by one. 
for i,row in data.iterrows():
    sql = “INSERT INTO `movies_details` (`” +cols + “`) VALUES (“ + “%s,”*(len(row)-1) + “%s)” 
    cursor.execute(sql, tuple(row)) 
# the connection is not autocommitted by default, so we must commit to save our # changes 
    connection.commit()