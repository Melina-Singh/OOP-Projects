from datetime import datetime, timedelta
from book import Book
from book_data import _BOOKS_DATA  # Import the _BOOKS_DATA variable directly

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self, category=None):
        print("Library Books:")
        for book in self.books:
            if category is None or book.category == category:
                print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book and book.available:
            book.available = False
            due_date = datetime.now() + timedelta(days=30)
            book.due_date = due_date.strftime("%Y-%m-%d")
            return book
        elif book and not book.available:
            return None
        else:
            return None

    def return_book(self, title):
        book = self.search_book(title)
        if book and not book.available:
            book.available = True
            book.due_date = None
            print(f"Thank you for returning {book.title}.")
        elif book and book.available:
            print(f"{book.title} is already available in the library.")
        else:
            print(f"Book with title '{title}' not found in the library. We don't have it, sorry.")

    def check_due_date(self, title):
        book = self.search_book(title)
        if book and not book.available and book.due_date:
            print(f"The due date for {book.title} is {book.due_date}.")
        elif book and not book.available and not book.due_date:
            print(f"{book.title} does not have a due date set.")
        elif book and book.available:
            print(f"{book.title} is available in the library.")
        else:
            print(f"Book with title '{title}' not found in the library. We don't have it, sorry.")
            

# Create Book objects and add them to the library
library = Library()
for book_data in _BOOKS_DATA: 
    book = Book(*book_data)
    library.add_book(book)
