#use of docstring
def reverse(str):
    '''FUNCTION USED FOR THE PURPOSE OF REVERSING THE STRING'''
    stack=[]
    for char in str:
        stack.append(char)

    rev=''
    while len(stack)>0:
        last=stack.pop()
        rev=rev+last
    return rev   
str=input('enter a string:-') 
result=reverse(str) 
print(reverse.__doc__)
print(reverse(str))