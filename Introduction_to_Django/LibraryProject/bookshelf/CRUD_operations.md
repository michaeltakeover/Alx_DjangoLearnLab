
>>> from bookshelf.models import Book
>>> books_to_delete = Book.objects.filter(title="1984")
>>> books_to_delete = Book.objects.filter(title="1984")
>>> books_to_delete.delete()
(2, {'bookshelf.Book': 2})
>>> print("Checking for remaining '1984' books after delete:")
Checking for remaining '1984' books after delete:
>>> print(list(Book.objects.filter(title="1984")))
[]
>>> print("\nRe-creating exactly one '1984' book...")

Re-creating exactly one '1984' book...
>>> book_1984 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(f"Newly created Book ID: {book_1984.id}")
Newly created Book ID: 6
>>> print("\nAttempting to retrieve the single '1984' book using .get()...")

Attempting to retrieve the single '1984' book using .get()...
>>> retrieved_book = Book.objects.get(title="1984")
>>> print(f"Book ID: {retrieved_book.id}")
Book ID: 6
>>> print(f"Title: {retrieved_book.title}")
Title: 1984
>>> print(f"Author: {retrieved_book.author}")
Author: George Orwell
>>> print(f"Publication Year: {retrieved_book.publication_year}")
Publication Year: 1949
>>> exit()
now exiting InteractiveConsole...