#values in set cannot be repeted
#sets are unordered and unindexed
#no way to change items in sets
b = set()
print(type(b))
#addign values in the set b
b.add(1)
b.add(2)
# b.add([5,7,9]) , #list cannot be added in the set as it is editibale
# b.add({5,7,9}) , cannot add dict in set
b.add((5,7,9)) #tuple can be used in set to add values
print(b)
print(len(b)) #items in b set. tupple, value, value
b.remove(2) # removes the value 2 from set
print(b.pop()) #removes one randon value from set

