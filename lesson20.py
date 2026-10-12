
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"{self.title} was written by {self.author} and has {self.pages} pages.")


book1 = Book("The Lion King", "John Smith", 120)
book2 = Book("The Eagle Eye", "Jane Doe", 200)
book3 = Book("The Survival of the Fittest", "Peter James", 350)

books = [book1, book2, book3]

for book in books:
    book.describe()
