#threading example to show multithreding in python 
import threading
from time import sleep
from threading import*

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1) # this will put the thread to sleep and class Hi to run 

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
t2.start()

t1.join() # because of join method , the main thread will print the bye after printing T1 and T2
t2.join()

print("Bye")

# Example 2
# Calculating squares and numbers of arrays
print("########## Example 2 ##########")
import time 
import threading

def calc_square(numbers):
    print("Calculate Square of numbers ")
    for n in numbers:
        time.sleep(1)
        print('square :- ', n*n)

def calc_cube(numbers):
    print("Calculate cube of numbers ")
    for n in numbers:
        time.sleep(1)
        print('Cube :- ', n*n*n)

arr = [2,3,4,5]

t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done in :", time.time()-t)