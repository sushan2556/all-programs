#what will be lenght of the this set
s= {20, 20.0, "20"}
# s= {20, 20.1, "20"} #will print lenght as 3 because 20 and 20.1 is diff
print(len(s))
# this will print the lenght as 2 because , 20 and 20.0 is considered as same value

s=set() #this betermines empty set
s={} #this determines empty dict
print(type(s))