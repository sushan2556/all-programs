num = int(input("Enter the no you want to check :-"))
sum = 0
new_no = num

while new_no > 0:
    element = new_no % 10 
    sum = sum+ element **3 
    new_no //=10

if num == sum :
    print("no is Amstrong")
else:
    print("No is not Amstrong")

# num = int(input("Enter the no you want to check :- "))
# sum=0
# new_no = num

# while new_no > 0:
#     element = new_no%10
#     sum = sum + new_no**3
#     new_no //= 10

# if num == sum:
#     print("The no is Amstrong")
# else:
#     print("The no is not Amstrong")

'''
print("########### armstrong number ################")

def amrstrng_no(num): #153
    sum = 0 
    new_no = num #new_no = 153
    while new_no>0: # num_no > 153
        element = new_no%10 # 153 % 10 = 15(element) , 3 stores in element
        sum = sum + new_no**3 # sum = 0 + (3**3)=27
        new_no //=10
    if num == sum:
        print("No is amtrong no ")
    else:
        print("no is not a amstrong no")

number = int(input("Enter a number to check: "))
amrstrng_no(number)
'''