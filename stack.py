# stack datastructure in python programming 
# stack of book , last book first book taken 
# lifo - last in first out 
# example - Browser session is in stack 

print("############## using a stack #################")

browser_data = []
browser_data.append(1)
browser_data.append(2)
browser_data.append(3)
print(browser_data)
if not browser_data:
    print("Disable")
else:
    browser_data.pop()
print(browser_data)
if not browser_data:
    print("Disable")
else:
    browser_data.pop()
print(browser_data)
if not browser_data:
    print("Disable")
else:
    browser_data.pop()
if not browser_data:
    print("Disable")
else:
    browser_data.pop()

# queue function is fifo or lifo 