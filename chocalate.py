'''We want to make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. 
Return -1 if it can't be done.'''



def make_chocalate (small, big, goal):
    if goal >= big * 5:
        remainder = goal - big*5
        print(remainder)

    else:
        remainder = big%5
    print ("the remainder is , " + str(remainder))
    
    if remainder <= small:
        return remainder
    else:
        return -1

print (make_chocalate(60, 100, 550))