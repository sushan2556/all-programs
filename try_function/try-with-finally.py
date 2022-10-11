# try clause with finally
# Python offers a finally clause which ensures execution irrespective of the exception

'''
try:
    code()
except :
    code()

finally:
    code() # this will be run irrespective of the exception
           # executes regardless of error

'''
try:
    i = int(input("enter a number: "))
    c = 1/5
except Exception as e:
    print(e)
    exit() #regardless of this finally will be run 

finally:
    print("Finally we are done") # this will be executed regardless of the error 

# finally will be run even after the code is exited !