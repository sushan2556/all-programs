from platform import python_branch
from re import A


s=set()
#empty set with set with parenthesis
print(type(s))

#set does not allow duplication 
s={1,2,2,3,3,4}
print(s)

#indexing and slicin not possible in set
s={1,3,"sushant"}
# print(s[0]) #'set' object is not subscriptable

#creating empty set 
s=set()
print(s)

#adding elements in set 
s={1,2,4,'python', 60}
print(type(s))
s.add('test') # add function add single element to the set
print(s)

#adding multiple element to the set
s={1,2,3}
s.update([4,6,'sushant']) #add multiple element to set using [] and update function 
print(s)
s.update(['shweta','test']) # adding multiple element in set using add function and square bracket
print(s)

bank={'citi', 'icici','hdfc', 'bob'}
print("deleting element in set using discard function")
print(type(bank))
bank.discard('bob')
print(bank)
print(id(bank))

#removing element using remove function 
bank={'citi', 'icici','hdfc', 'bob'}
bank.remove('citi')
print(bank)
# bank.remove('citi') # remove will give error if the key is not in the set
bank.discard('citi') #discard will not give error even even if the element is not present in the set

# accessing set using for loop
s={20, 30, 'Jeep', 'tesla'}
for i in s:
    print(i)

print('#############################################')

# s=set()
# print(id(s))
# print(type(s))
# count = int(input("enter the no of elements --> "))
# for i in range(count):
#     el = int(input('enter the elements --> '))
#     s.add(el)
# print(s)

#clear method in set

s={10,20,30}
print(type(s))
print('before clear', s)
s.clear()
print('after clear',s)

#######################

#intersection of sets , return items that exists in both set

a = {'Sachin','rahul','sourabh'}
b = {'Sachin', 'Mahendra', 'yuvrag'}
print('A:', a)
print('B:', b)
print()

intersection = a.intersection(b)
print(intersection)

# Union of set return all element from original set as well as specified set 

union = a.union(b)
print(union)

#Diference method, return elements that only exist in first set and not in the second set 
difference = a.difference(b)
print(difference)

#issubset return true if all element in the set exist in the specified set
subset = a.issubset(b)
print(subset)

#issuperset - return true if all item in the specified set exists in the original set
issuper = a.issuperset(b)
print(issuper)

# Copy command in python
a = {1,2,4,3}
print('Before copy ', a)
print(id(a))
new_a = a.copy()
print('After copy ',new_a)
print(id(new_a))

#passing set to function 

def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)

a_set={1,2,3,54,6,7,6}
show(a_set)

#pass and return set
def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)
    return s
st = {2, 'practise', 7, 'test'}
new_st = show(st)
print(new_st)
print(type(new_st))