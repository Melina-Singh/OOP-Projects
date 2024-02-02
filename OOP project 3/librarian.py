# ya changes needed

from library import Library

class Librarian: #🙎‍♂️
    def __init__(self, library):
        self.library = library

    def provide_book(self, title):
        book = self.library.borrow_book(title)
        if book:
            print(f"Librarian: Here is '{book.title}'. Please return it by {book.due_date}.")
        else:
            print("Librarian: I'm sorry, we don't have that book or it's currently not available.")

    def check_due_date(self, title):
        self.library.check_due_date(title)
