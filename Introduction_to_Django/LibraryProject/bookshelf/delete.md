# First, retrieve the book to delete (only if it's not already in the shell)
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()
# (1, {'yourapp.Book': 1})  # Replace 'yourapp' with your actual app name

# Confirm it's deleted
Book.objects.all()
# <QuerySet []>