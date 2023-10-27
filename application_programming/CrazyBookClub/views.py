from django.shortcuts import render

from .models import Book, Review

# Create your views here.

def index(request):
    # The home page for CrazyBookClub
    return render(request, 'CrazyBookClub/index.html')

def books(request):
    # Show all books
    books = Book.objects.order_by('date_added')
    context = {'books': books}
    return render(request, 'CrazyBookClub/books.html', context)

def reviews(request):
    # Shows all the reviews
    reviews = Review.objects.order_by('date_added')
    context = {'reviews': reviews}
    return render(request, 'CrazyBookClub/reviews.html', context)