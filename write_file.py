# write a new file 
f = open("another_file.txt", "w") # w is when you need to write and a is when you need to append file
f.write("append this to the file")
f.write("2nd append this to the file")
f.close

'''
modes of file function 

w = write the file
w moxe can be used multiple times before closing the file, but it will overwrite the file everytime

a = append the file
append will update the file with existing data

r = reading
just to read the file

+ = updating the file

rb = is to open the file in binary mode
rt = is to open the file in text mode, default is rt
'''