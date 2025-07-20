from bookshelf.models import Book  # Import the Book model

# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()
# (1, {'bookshelf.Book': 1})  # Confirms one object deleted

# Confirm deletion
Book.objects.all()
# <QuerySet []>