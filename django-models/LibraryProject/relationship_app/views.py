from django.shortcuts import render
from .models import Book
from .models import Library
# Create your views here.


def book_list(request):
    books = Book.objects.all().select_related('author')
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

#class LibraryDetailView(DetailView):
