'''
from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3

# print the enum member
print(Day.MONDAY)

# get the name of the enum member
print(Day.MONDAY.name)

# get the value of the enum member
print(Day.MONDAY.value)
'''

# from enum import Enum
#     class Color(Enum):
#          RED = 1
#          GREEN = 2
#          BLUE = 3
#     print(Color.RED)


from enum import Enum

class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3
for shake in Shake:
    print(shake)