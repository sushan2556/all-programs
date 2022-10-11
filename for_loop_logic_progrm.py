# create a list of subjects

data = ["Java", "Python", "Html","PHP"]
print("indexes in the list :-")
#display the indices in the list
for i in range(len(data)): 
    print(i)
print("Index value in the list:-")
for i in range(len(data)):
    print(data[i])

print('##################################################')
list_1 = ["Java", "python", "HTML", "PHP"]
for i in range(len(list_1)):
    element = list_1[i]
    print(i, element)

print("####################################################")
#program to find the sum of all numbers stored in the list 

list1 = [2,3,4,5,6,7] 
sum = 0 #variable to store the sum
for i in list1: #iterate over the list using for loop
    sum = i+sum
print(f"The sum of the values in list is -> {sum}")

print("############ print individual letters of string using for loop################")
s = ("Sushant")
print(type(s))
for i in s:
    print(i)

print("########## Nested for loop##############")

list2 = ['element1', 'element2', 'element3']
for i in range(len(list2)):
    for j in range(len(list2[i])):
        print(j,list2[i][j])