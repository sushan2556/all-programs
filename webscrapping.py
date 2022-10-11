
# Requests library is used for making HTTP requests to a specific URL and returns the response. 
# Python requests provide inbuild functionalities for managing both the request and response.

'''
# Making a get response 
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
print(r)
print(r.url)
print(r.status_code)

# beautiful soup library is used to extract information from html and xml files . It provides a parse tree and 
# the function to navigate , search or modify this parse tree.

# Parsing the HTML content . This creates a parse tree 
soup = BeautifulSoup(r.content,'html.parser') # html parser we have used over here 
# print(soup.prettify()) # this will create a readable html code for us 
print(soup.title.name) # to pull the title from the parser file 
print(soup.title.parent.name)
s = soup.find('div',class_='entry-content')
content = s.find_all('p')
print(content)
'''

import requests
from bs4 import BeautifulSoup
# Web scrapping example 

# making a get request
r = requests.get('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm')

# print(r.content) # will print the content of the page 
# print(r.url)
# print(r.status_code)

soup = BeautifulSoup(r.content,'html.parser')
# print(soup.prettify)

#getting the title tag 
# print(soup.title.name)

movie_rating = []

s = soup.find('div', class_='lister')
lines = s.find_all('a')
for line in lines:
	print(line.text)

s1 = soup.find('div', class_='lister')
lines1 = s.find_all('strong')
for line1 in lines1:
	print(line1.text)

movie_rating.append ({ line.text: line1.text })
print(movie_rating)
