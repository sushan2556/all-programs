#practising build in functions/modules

l = ['Dan','shweta','sushant']
l2 = [1,2,4,5,6,7,8]
print(type(l)) 
print(dir(l))
print(sorted(l))
print(max(l))
print(min(l))
print(id(l))

n = -456
print(abs(n))
#returns abs value of num

x = pow(3,4)
print(x)
# returns 3x3x3x3 
y = pow(3,4,5)
print(y)
#returns 3x3x3x3 %5 reminder of 81/5

t = (1,6,3,8,0,3,4,9)
print(sorted(t))
#sort will sort the method in tuple 

x = ord('d')
print(f"The ord of d is {x}")
# returns the unicode of the character , every alphabet has a unicode in python 
print(len(l2))

s = "sushant"
print(len(s))
# print(help(t))

# finding factorial of number , nx3x2x1

# using for loop 
# num = int(input("Enter the number to find factorial:- "))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial * i
# print(f"The factorial using for loop is {factorial}")

# #using while loop ... for while loop , counter --> condition --> increment counter 
# num = int(input("Enter the number to find factorial:- "))
# facto = 1
# while num >0:
#     facto = num * facto
#     num -= 1
# print(f"The factorial using while loop is {facto}")

#using recursion method , calling the function recursively 
# def facto(n):
#     if n==1:
#         return 1
#     else:
#         return n * facto(n-1)

# n = int(input("Enter no :- "))
# print(f"The factorial using recursion function of {n} is {facto(n)}")

#using decorator
#convert list to dictinary with list comprehension
list=[1,'b','3',2,'3 ' ,'r',33,44]
dict2={n:list[n] for n in range(len(list))}
print(dict2)    

# list to set without comprehension 
sample_list = [2,3,4]
sample_set = set(sample_list)
print(sample_set)
tuple_1 = tuple(sample_list)
print(tuple_1)
print(type(tuple_1))

# aTuple = (True, 28, 'Tiger')
# print(type(aTuple))
# aList = list(aTuple)
# print(type(aList))
# print(aList)
print("#######################")
list1 = ['sushant','Shweta']
# string1 = str(list1)
# print(string1)
# print(type(string1))

# dict1 = dict(list1)
# print(dict1)

# convert string linto list 
s = "Sushant" #string
lst = {} # emoty dictionary 
for i in range(len(s)): # for loop with lenght of string 
    lst[i]=s[i] # key(index as per the string) -- value(elements in the string)
print(lst) 

print("##########################")
s1 = "Shweta"
s2 = "asdfga"
# it = iter(s1)
dict1 = {s1:s2}
print(dict1)
print(type(dict1))
print("#################################")
lst2 = [1,2,3,4,5,6]
# convert list into dictionary
# # dict = {} 
# for i in range (len(lst2)):
#     dict[i]=lst2[i]
# print(dict)

print("#######################")
#convert tuple into dict
tuple1 = (6,5,4,3,2,1)
dict4 = {}
for i in range(len(tuple1)):
    dict4[i]=tuple1[i]
print(f"converting tuple {tuple1} to dictioanry {dict4}")

print("##################################################")

#using while loop
tuple11 = (7,6,47,32,29,14)
i = len(tuple11)
dict5 = {}
while i < 6:
    dict5[i]=tuple11[i]
    i=+1
print(f"converting tuple to dict using while loop {dict5}")

'''
GIT repository we pushed our code 
BA connection with developer using jenkins
Continue integration continue developement
jenkins is plugin tool 
'''
print("####################################333")
# List comprehension examples 
list2=[]
for i in range(10):
    list2.append(i)
print(list2) 
#using comprehension
list3 = [i for i in range(10)]
print(list3)
list4 = [i for i in tuple11 if i%2==0]
print(list4)

print("##############################3")
#using list comprehension 
def convert_lst(lst_2):
    result_dict = {lst_2[i]:lst_2[i+1] for i in range(0,len(lst_2),2)}
    return result_dict
lst_2 = ['element1' , 'element2', 'element3', 'element4']
print(convert_lst(lst_2))

#using zip() method
# def zip_method(lst4):
#     it = iter(lst4)
#     res_dict = dict(zip(it,it))
#     return res_dict

# lst4 = [3,4,6,8]
# print(zip_method(lst4))

# Python3 program to Convert a
# list to dictionary

# def Convert(a):
# 	it = iter(a)
# 	res_dct = dict(zip(it , it))
# 	return res_dct
		
# # Driver code
# lst = ['a', 1, 'b', 2, 'c', 3]
# print(Convert(lst))

#using zip methods
index = [1,2,3]
language = ['python', 'c', 'c++']
d1 = dict(zip(index, language))
print(d1)

#list to dict using dictionary comprehension 
print("####################################")
l1 = [8,4,5,6,7,4]
print({l1[i]:l1[i+1] for i in range (0,len(l1),2)})

l2 = ['sushant', 'looks good', 'Shweta', 'looks decent']
#using dictionary comprehension 
print({l2[i]:l2[i+1] for i in range(0,len(l2),2)})
#using iterator
it1 = iter(l2)
for i in range (len(l2)):
    res_dict1 = dict(zip(it1,it1))
print(res_dict1)
#using enumarate function
l3 = [8,3,4,5,6,7]
print({i:j for i,j in enumerate(l3,1)})
l4 = ['a','b','c','d']
com = print({i:l4[i] for i in range(len(l4))})
l5 = (1,2,3,4,5,6)
print({i:l5[i] for i in range (len(l5))})