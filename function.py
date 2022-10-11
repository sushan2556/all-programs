# function exaple 
def percentfunc(marks):
    return(((marks[0] + marks[1] + marks[2] + marks[3])/400) * 100)


marks1 = [32, 45, 56, 89]
percentage1 = percentfunc(marks1)

marks2 = [92, 65, 89, 34]
percentage2 = percentfunc(marks2)

print(percentage1,percentage2)