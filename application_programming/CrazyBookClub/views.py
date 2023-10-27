from django.shortcuts import render, redirect

from .models import Book, Review
from .forms import BookForm, ReviewForm

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

def new_book(request):
    # Add a new book.
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BookForm()
    else:
        # POST data submitted; process data.
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('CrazyBookClub:books')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'CrazyBookClub/new_book.html', context)

def new_review(request):
    # Add a new review.
    if request.method != 'POST':
        form = ReviewForm()
    else:
        # Post data submitted; process data.
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('CrazyBookClub:books')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'CrazyBookClub/books.html')