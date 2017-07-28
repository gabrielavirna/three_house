"""Constructors - class methods"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)


class BookCase:
    def __init__(self, books=None):
        self.books = books

    @classmethod    # decorator
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books)

# bc = BookCase()
bc = BookCase.create_bookcase([('Moby-Dick', 'Herman Melville'), ('Jungle Book', 'Rudyard Kipling')])
print(bc)
print(bc.books)
print(bc.books[0])
print(str(bc.books[0]))