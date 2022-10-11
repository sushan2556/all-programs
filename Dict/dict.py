# empty dict

d2={101: 'sushant', 102: 'sakshi', 103: 'mayuri', 104: 'rahul', 106: 'abhay',
107: 'sanika', 'name': 'rahuk', 'lastname': 'dhokane'}
print(d2.pop('name'))
print(d2)

key=[1,2,3]
value=['python',2,3]
d=d2.fromkeys(key,value)
print('new dict',d)

#get method in dict - it is used to get single value from the key
d1={'key1':"value1", 'key2':'value2', 'key3':'value3'}
print(d1)
print(d1.get('key1'))
print(d1.get('key2'))

#items method in dict --> to get all key and values in the form of tuple 
it=d1.items()
print(it)

it2=d2.items()
print(it2)

# update method in dict --> will update the value of specific key
print(d1)
up=d1.update({'key1':'value1new'})
print(d1)
print('############################################')
#update function use to update the exsting dict with key and value 
d={'name':'sane','lastname':'guruji'}
print(d)
print("d1 dict before update",d1)
print(d1.update(d))
print(d1)

#pop method --> pop method provided the key will pop the key and value from the dictionary
print('POPPOPOPOPOPOPOPOPOPOPOPOPOPOPOPOPOPOOPOPOPOPOPOP')
d2={101: 'sushant', 102: 'sakshi', 103: 'mayuri', 104: 'rahul', 106: 'abhay',
107: 'sanika', 'name': 'rahuk', 'lastname': 'dhokane'}
print(d2)
print(d2.pop('lastname')) 
(print(d2))
print('popitem','popitem','popitem','popitem','popitem','popitem','popitem')
#pop item method in dictionary --> will remove item as tuple 
d2={101: 'sushant', 102: 'sakshi', 103: 'mayuri', 104: 'rahul', 106: 'abhay',
107: 'sanika', 'name': 'rahuk', 'lastname': 'dhokane'}
print(d2)
print(d2.popitem())
# print(d2)