#multi line string 
from itertools import count
from re import T


s='''this ia a multi line string ,
    for example of string'''
print(type(s))

s="Today is a good day to work on python"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[-1]) # starts fom last element of the string 
print(s[::-1]) # prints the string in reverse mode

# item assignment in string 
s="Today is a good day to work on python"
# s[0]="d" #string object does not support item assignment
print(s)

#string concatination 
s1="today is "
s2="a good day"
s3="to start learning"
print(s1 + s2 + s3) # string concatination is possible 
print(s3 + s1 + s2)
#length of string
print(len(s))
# membership operator in string
s="Today is a good day to work on python"
print("today" in s.lower()) #case sensitive , we can use lower case to change and find the word 
print('tomorrow' is not s) #is not membership operator

print('****************************************************')

#Methods in string 
#count()
s='this is a string to use function count'
# print(s.count('t')) # counts the number of t elements in the string 
print(s.count('this')) 
#replace 
print(s.replace('function count', 'count function'))

#case in string 
s='TO TEST THE CASE METHODS IN STRING '
print(s.capitalize()) # capitalise the first letter in the elment
print(s.endswith("method")) # to find if the string ends with the provided value
print(s.swapcase()) # swaps the case of the string 
print(s.title()) # capitilise first element of all the string
print(s.casefold()) # returns the string where all the character are in lower case
print(s.startswith("to"))
print("#######################################################")
s="12345"
print(s.isalnum()) # prints true if the string contains all numbers
s="Sushant"
print(s.isalpha()) # prints if the string contains all alphabets

#string formating

s='Sunders'
s1='100k dollars'
s3='Google'
print(s, 'salary is ' ,s1, 'working at ' ,s3)

#using f string
print(f"{s} salary is {s1} working at {s3}")

#using .format
print('{} salary is {} working at {}'.format(s,s1,s3))

# length of string using len function 
s='to test the length function'
print(len(s))


#using len function in string 
s = 'testing the lenght function in string '
print(len(s))
for i in s:
    print(i) #item slicing is not possible to pull single element in string 

s = 'removing the blank spaces using for loop in string'
for i in range(len(s)):
    if s[i]==' ': # if the element is blank space 
        continue
    print(i,s[i])

#split function in python - it converts string to list
s='testing the split function'
l=s.split()
print(l)
print(type(l))

# access charater using slicing 
str = 'testing the slicing function'
print(str[0])
print(str[4])

#access charater of string without index
str1 = 'accesing charater of string'
for i in str:
    print(i)

# access charater of string with index and charater 
str2="accesing charater and index of this string"
for i in range(len(str2)):
    print(str2[i], "=" ,(i))

#access using while loop with index and charater 
str3= "to test while loop and access charater and index"
i=0
while i < len(str3):
    print(str3[i], '=', i)
    i+=1

#string is immutable , item assignment is not possible
# str4 = 'item assignment in python'
# str4[0]='f' #TypeError: 'str' object does not support item assignment
# print(str4)

#repetition operator in string 
str5 = 'testing repetation in string '
print(str5[4]*3)
print(str5*5)

#concatination in string 
str1= 'test'
str2 = 'test1'
print(str1 +' '+ str2)

