# using string replace function to replace name and date
letter = '''Dear <|NAME|>
Greetings for today !
we are happy to inform you that, you have been selected.
your joining day is <|DATE|> '''
name = input("Enter your name\n") 
date = input("enter todays date \n")
letter=letter.replace("<|NAME|>", name)
letter=letter.replace("<|DATE|>", date) 
print(letter)