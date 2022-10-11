# l1=[1,8,7,2,21,15]
# print(l1)
# l1.sort() , '''sorting the list in ascending order'''
# l1.reverse() , '''sorts the list in descending order'''
# print(l1)
# l1.append(45) , '''adds the number to the end of the list'''
# l1.insert(2,545) , '''inserts the value on 0 index. index, value'''
# print(l1)
# l1.pop(2) #removes the index 2 elements from the list
# l1.remove(21) #removes the 21 value from the list
# print(l1)


############## accepting user input and creating list or tuple ###########
values=input("enter values sperated with comman : ") # input is in string
list = values.split(",") # split method with split the string into a list
tuple = tuple(list) #tuple will create a tuple out of the list
print("list : ",list) # print list 
print("tuple : ",tuple) # print tuple 

##### write a python programe to print first and the last colour from the list #############
list2 = ["red", "green", "blue", "black"]
print(f"the first colour in the list is {list2[0]} and last colour in the list is {list2[1]}")
