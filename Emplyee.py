# class attribute and instances 
class Employee(): # class 
    company = "google" # class attribute
    salary = 100

Sushant = Employee()
Shweta = Employee()
Sushant.salary = 45
# Shweta.salary = 200
print(Sushant.company)
print(Shweta.company)
print(Sushant.salary) # this ill print the instance attribute first even if it is under class attribute
print(Shweta.salary)

# Employee.company = "Youtube" # creating company instance of Employee
print(f"The salary for Sushant is {Sushant.salary} and company is {Sushant.company} ")



