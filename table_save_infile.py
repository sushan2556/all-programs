num = int(input("Please enter a number : "))

table = [num*i for i in range(1, 11)] # list comprehension 
print(str(table))

with open ("tables.txt", "a") as f:
    f.write(str(table))
    f.write('\n')
