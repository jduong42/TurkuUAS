from django.shortcuts import render

from .models import Book

# Create your views here.

def index(request):
    # The home page for CrazyBookClub.
    return render(request, 'CrazyBookClub/index.html')

def books(request):
    # Show all books.
    books = Book.objects.order_by('date_added')
    context = {'books': books}
    return render(request, 'CrazyBookClub/books.html', context)

def book(request, book_id):
    # Show a single book and all its entries.
    book = Book.objects.get(id=book_id)
    entries = book.review_set.order_by('-date_added')
    context = {'book': book, 'entries': entries}
    return render(request, 'CrazyBookClub/book.html', context)