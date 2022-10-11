#program to find of the entered marks pass the student or fail them
sub1 = int(input("Enter marks of sub 1: "))
sub2 = int(input("Enter marks of sub 2: "))
sub3 = int(input("Enter marks of sub 3: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are failed as one of the subject has less marks than 33")
elif(sub1 + sub2 + sub3 )/3 < 40:
    print("you are failed as the percentage is less than 40")
else:
    print("You are passed")