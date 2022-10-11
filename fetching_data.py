# Connecting to mysql database
import pymysql
import numpy as np
import matplotlib.pyplot as plt


mydb = pymysql.connect(host="localhost",
							user="Root12",
							password="Root12!@",
							database="cricket")
mycursor = mydb.cursor()

# Fecthing Data From mysql to my python progame
mycursor.execute("select Player_name, Runs from cricket_team")
result = mycursor.fetchall

Player_name = []
Runs = []

for i in mycursor:
	Player_name.append(i[0])
	Runs.append(i[1])
	
print("Name of Player = ", Player_name)
print("Runs of player = ", Runs)


# Visulizing Data using Matplotlib
plt.bar(Player_name, Runs)
plt.ylim(100, 900)
plt.xlabel("Name of Employee")
plt.ylabel("ID's of Employee")
plt.title("Employee information")
plt.show()
