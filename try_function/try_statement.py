# exception handling with try statement
# 
while(True):
    print("Press q to quite")
    a = input("Enter a number :")
    if a == 'q':
        break
    try:
        print("Trying ..")
        a = int(a)
        if a>6:
            print("The number is greate than six")
    except Exception as e:
        print(f"your input resulted in an error {e}")

print("Thank you for playing this game !")
