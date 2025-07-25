import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()
from relationship_app.models import Author, Book, Library, Librarian

author_name = "Amiegbe Osayande Michael"


try:
    author = Author.objects.get(name=author_name)

    books = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    
    for book in books:
        print(f"- {book.title}")
    
except Author.DoesNotExist:
    print(f"No author found with the name '{author_name}'.")

# List all books in the library
print("\nAll books in the library:")
books = Book.objects
books = books.all()
for book in books:
    print(f"- {book.title}")

# Retrieve the librarian for a library
library_name = "Central library"
try:
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"\nLibrarian for '{library.name}.: {librarian.name}")
except library.DoesNotExist:
    print(f"\nNo library found with the name '{library.name}'.")
except Librarian.DoesNotExist:
    print(f"\nNo librarian assigned to '{library_name}'.")

