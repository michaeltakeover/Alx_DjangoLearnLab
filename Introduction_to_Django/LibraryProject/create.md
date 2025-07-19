from books.models import Book
book = Book.objects.create(title="1984", author="George Orwell", year=1949)
book