class Book:
    """A class that represents a book"""
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"{self.title.title()} by {self.author.title()} (Genre): {self.genre.title()}"

class Library:
    def __init__(self):
        # Empty List to store book objects
        self.books = []


    def add_book(self, book):
        """ Adds a new book to the library"""
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def remove_book(self,title):
        """Removes a book from the library by title"""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Book "{title}" removed from the library.')
                return
        print(f'Book "{title}" not found in the library.')

    def display_books(self):
        """Displays all the books in the library"""
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library: ")
            for book in self.books:
                print(book)

library = Library()



book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
book2 = Book("1984", "George Orwell", "Dystopian")
book3 = Book("To Killing a Mockingbird", "Harper lee", "Classic")

print()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_books()

print()
library.remove_book("1984")
library.display_books()
