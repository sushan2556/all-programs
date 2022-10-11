#A list contains the multiplication table of 7. write a programe to convert it to a vertical string of same numbers

l = [str(i*7) for i in range (1, 11)] # using list comprehantion created a table of 7 , list contains integers in it default
print("horizontal value of the table ", l )
vt = "\n".join(l)  #using join function we added \n to print the table vertically
print("The vertical ouput of the table ", vt)