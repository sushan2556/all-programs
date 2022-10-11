# regular expressions in python
import re
mystr = '''What is String in Python?
A string is a sequence of characters.
A character is simply a symbol +91 9860653218. For example, the English language has 26 characters.
Computers do not deal with characters, they dealdeal with numbers (binary). 
Even though you may see characters on your screen, internally it is stored and manipulated as a combination 
of 0s and 1s. This conversion of character 020-12345678 to a number is called encoding, 
and the reverse process is decoding. ASCII and Unicode are some of the popular encodings used.
In Python, a string is a sequence of Unicode characters. Unicode was introduced 
to include every character in all languages and bring uniformity in encoding. You can learn about 
Unicode from Python Unicode.'''

# function in regular expression --> findall, split, sub, finditer

pattern = re.compile(r'deal') # finding deal in the raw string
# pattern = re.compile(r'.') # any character
# # pattern = re.compile(r'.acter') # acter followed after any character
# pattern = re.compile(r'^What') # ^ means start with
# pattern = re.compile(r'Unicode.$') # $ means string ends with
# pattern = re.compile(r'ASCI*') # it finds ASC and any no of I in the str
# pattern = re.compile(r'ASCI+') # one one or more occorance of I
# pattern = re.compile(r'ASCI{2}') # exact no of occorance of charcter I
# pattern = re.compile(r'internal{2}') # will find where l is 2 times
# pattern = re.compile(r'(deal){2}') # will find a grou where deal is mentioned twice
# pattern = re.compile(r'I{2}|deal') # | this stands for either or

#Special sequences
# pattern = re.compile(r'\AWhat') # \A if the str starts with what
# pattern = re.compile(r'\Bracter') # where the racter word is present in middle
# pattern = re.compile((r'\bFor')) # where it starts with word For anywhere
# pattern = re.compile((r'symbol\b')) # where it end with word For anywhere
# pattern = re.compile(r'\d{3}-\d{8}')
pattern = re.compile(r'\b.+91 \d{10}')

matches = pattern.finditer(mystr)
for i in matches:
    print(i)
