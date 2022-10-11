# student library using OOP
# can borrow and returm books

class Library:  # Library is real word entities
    def __init__(self, listOfBooks) -> None:
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are : ")
        for book in self.books:
            print(" * " + book)

    def barrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} book.")
            self.books.remove(bookName)
            return True
        else:
            print("this is already issued to someone else")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"Thanks for returning {bookName}")


class Student:  # Student is real word entities
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Algo", "Java", "testing", "jungle"])
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = ''' ===== Welcome to the central library =====
        1. List of books
        2. Request a book
        3. Return a book
        4. Exit
        '''
        print(welcomeMsg)

        a = int(input("Enter a choice : "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.barrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thank you for using the library")
            exit()
        else:
            print("Invalid choice ")

