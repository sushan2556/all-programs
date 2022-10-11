# for loops in python, it is used to iterate through a sequence in list, tuple or string [iterables]
# example
#print list valies using for loop


fruit = ["mango", "banana", "chiku", "grapes"]
for item in fruit:
    print(item)

print("##########################################")
l=[[1,2,3,4],[5,6,7,8]]
n=len(l)
print('length of list',n)
for i in range(n):
    m=len(l[i])
    # print(m)
    for j in range(m):
        # print(j)
        print('outer index:->',i,'inner index:->',j,'element:->',l[i][j])