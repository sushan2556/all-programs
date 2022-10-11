# write a programe to filter a list of numbers which are divisible by 5

l = [2, 50, 29, 12, 109]

by5 = filter(lambda num: num%5==0, l)

print(list(by5))


# using functions
# def divisileByFive(num):

#     if num % 5 == 0:
#         return (num)
#     else:
#         print("No such numbers")


# print(list(filter(divisileByFive, l)))
