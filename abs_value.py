'''Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), 
while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the 
absolute value of a number.

'''

'''def close_far(a, b, c):
  if abs(b-c)>=2:
    if (abs(a-b)<=1 and abs(a-c)>=2) or ( abs(a-c)<=1 and abs(a-b)>=2):
      return True
  return False

print(close_far(10, 8, 9))'''


def close_far(a,b,c):
    if abs(b-c)>=2:
        if abs(a-b) <=1 and abs(a-c)>=2 or abs(a-c) <=1 and abs(a-b)>=2:
            return True
    return False

print(close_far(-1, 10, 0))