
# join methods = creates a string from your iterable objects 

l = ["camera", "Laptop", "Phone"] # created list with name as l
l1 = ("camera", "Laptop", "Phone") # tuple  created tuple with name as l1

newstr = ' and '. join(l1) # --> new variable as newstr which will join "and" to l1 tuple
newstr2 = ' '.join(l)  # --> new variable as newstr2 which will join " " to l list

print(newstr)
print(newstr2)