from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Shows these columns
    list_filter = ('publication_year', 'author')            # Adds filters on the side
    search_fields = ('title', 'author') 
    
# Register your models here.
admin.site.register(Book)

