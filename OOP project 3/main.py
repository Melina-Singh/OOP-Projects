# from here i access all the information i need from every classes
from library import library
from librarian import Librarian

# thisis the object of Librarian class
librarian = Librarian(library)

# User and  librarian interaction
user_request = input("User: Can I borrow 'Clean Code'? (yes/no): ").lower()
if user_request == "yes":
    librarian.provide_book("Clean Code: A Handbook of Agile Software Craftsmanship")
    librarian.check_due_date("Clean Code: A Handbook of Agile Software Craftsmanship")
else:
    print("User: Okay, maybe next time.")

# Display all books
# library.display_books()

# this information shoulb be displayed after returning the book 
# library.return_book("Clean Code: A Handbook of Agile Software Craftsmanship")

 # 
# library.display_books()
