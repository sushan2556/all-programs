# greeting="Good Morning "
# name = "Sushant"
# print(type(name))
# print(greeting+name)
# c = greeting + name , '''concatinating two string'''
# print(c)
name = "Sushant"
# print(name[6]) , '''[] square bracket counts the index of string, from 0 to lenght -1'''
# print(name[0:5]) , '''string slicing '''
# negative slicing/indexes to be done using -1
# print(name[-1])
# string slicing with skip value
print(name[1:6:2]) , '''skiping the second number'''
print(name[::-1])

s='today is good day to learn python'
print(s.startswith('tsoday'))
print(s.endswith('python'))

print("##########################")
s='today is good day to learn python'
for i in range(len(s)):
    if s[i]==' ':
        continue
print(i,s[i]) 

l=s.split(' ')
print(l) 
print(type(l))