# write a program to print the following pattern
'''

***
* *
***

'''

# rows = 3

# for i in range(rows): # i will be executed for 0,1 and 2 times as per index
#     if (i == 0 or i == rows-1):
#         print('*'*rows)
#     else:
#         print('*' + ' '*(rows-2) + '*')


# write a program to print the following pattern
'''

***
* *
***

'''

row=3

for i in range(row):
    if i == 0 or i == (row-1):
        print('*'*(row))
    else:
        print('*'+' '*(row-2)+'*')

