# pythom time module to calculate elapsed time 

# from os import stat_result
from timeit import default_timer as timer
import time

a = 50
b = 60

# start = time.time()
start = timer()
sum = (a+b) *(a*b) 
print(sum)
end = timer()