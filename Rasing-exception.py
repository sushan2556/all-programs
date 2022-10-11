def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good Sushant")
    
a = increment('asd')
print(a)

'''
try with else clause 

try :
    try ()
except:
    #some code 
else :
    code() #this will execute if the try code is run and the programe did not entered the except clause

'''