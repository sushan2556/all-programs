# creation of series 

import pandas as pd
import numpy as np
import csv 
#first way to create series from scalar values 
series1 = pd.Series([1,2,3,4,5])
print(series1)
print(type(series1))

#second way creation of series using numby array

series2 = np.array([1,2,3,4,5])
print(series2)
print(type(series2))

#creation using dictionary 
dict1 = {'India':'Delhi', 'UK':'London','Australia':'Sydney','Sigapore':'Qualalumpur'}
series3 = pd.Series(dict1)
print(series3)
print(type(series3))

#accesing elements of series 

print(series3['India'])
print(series3[1]) #indexing
print(series3[2])

print(series3[0:4]) # index of keys 

# mathematical operations on series 
# addition of series 
print(series1+series2) # additions of values 
# if both series do not have same no of element the addition will include a nan value 
print(series1*series2)

# dataframe in python / SQL
# creation of dataframe
import pandas as pd
d = pd.DataFrame()
print(d)
print(type(d))

# creation of dataframe using numby array
array1 = np.array([1,2,3])
array2 = np.array([100,200,300])
array3= np.array([1000,2000,3000,4000])

dframe = pd.DataFrame([array1,array2,array3])
print("################")
print(dframe)
print("################")

#creation of dataframe using list of dictionary
listofdict = [{'a':'1','b':'2','c':'3'},{'4':'d','5':'e'}]
dframe1 = pd.DataFrame(listofdict)
print(dframe1)

csv_data = dframe1.to_csv(sep='|')
print(csv_data)