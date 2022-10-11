# program to find simple interest 

'''
p*t*r/100
'''
principle = int(input("Enter the principle amount :- "))
time = int(input("Enter the time eperiod :- "))
rate_of_interest = float(input("Enter the rate of interest :- "))

simple_interest=((principle*time*rate_of_interest)/100)

print ("The simple interest is :- ",simple_interest) 
print(f"The simple interst is {simple_interest}")


def simple_interest(a,b,c):
    x = (a*b*c)/100
    print(f"The simple interest is {x}")

principle = int(input("Enter the principle amount :- "))
time = int(input("Enter the time eperiod :- "))
interest = float(input("Enter the rate of interest :- "))

simple_interest(principle,time,interest)

