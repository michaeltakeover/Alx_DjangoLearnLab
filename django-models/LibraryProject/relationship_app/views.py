from django.shortcuts import render
from .models import Book, Library
from django.views.generic import ListView, DetailView
# Create your views here.


def book_list(request):
    books = Book.objects.all().select_related('author')
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)


class BookListView(ListView):
    model = Library
    template_name = 'list_books.html'
    context_object_name = 'library'

#class LibraryDetailView(DetailView):
