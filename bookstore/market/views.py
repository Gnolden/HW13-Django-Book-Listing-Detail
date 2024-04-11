from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Book

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Book

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 3)  # Display 3 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'market/book_list.html', {'page_obj': page_obj})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'market/book_detail.html', {'book': book})
