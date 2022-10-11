# from typing import Mapping


def greet(name):
    print(f"Good Morning, {name}")

if __name__ == "__main__": # this will check if the code is run in the main file and not in the imported file if any
    n = input("Enter a Nmae : \n")
    greet(n)