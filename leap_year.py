#find out leap year 



def leap_year(year):
    if (year % 400 == 0) or (year % 4 ==0 and year % 100 != 0):
        return True
    else:
        return False

n = int(input("Enter the year:-"))
print(leap_year(n))

'''
if year is divisible by 400 then is_leap_year
else if year is divisible by 100 then not_leap_year
else if year is divisible by 4 then is_leap_year
else not_leap_year
'''