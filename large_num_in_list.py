#find the largest num in list 

lst1 = [99,4,6,3,1]
large_no = 0
n = len(lst1)
i = 0
while i<n:
    if large_no<lst1[i]:
        large_no = lst1[i]
    i+=1
print(large_no)

# lst=[11,22,33,44,121,4,4,6,676,88]
# large_num=0
# n=len(lst)
# i=0
# while i<n:
#     if large_num<lst[i]:
#         large_num=lst[i]
#     i+=1
# print(large_num)