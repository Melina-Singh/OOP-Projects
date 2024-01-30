
class Book:
    def __init__(self,title, author, category, ISBN):
        self.title = title
        self.author = author
        self.category = category 
        self.ISBN = ISBN
        self.available = True
        self.due_date = None

    def __str__(self):
       
       book_info = f"Title: {self.title}\nAuthor: {self.author}\nCategory: {self.category}\nISBN: {self.ISBN}\nAvailable: {self.available}"


       if not self.available:
        if self.due_date:
           book_info += f"\nDue Date: {self.due_date}"
        else:
            book_info += "\nDue Date: Not set"

       return book_info

