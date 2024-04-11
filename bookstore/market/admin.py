from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    search_fields = ['name', 'author_name']

admin.site.register(Book, BookAdmin)
