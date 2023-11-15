from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Book, Review
from .forms import BookForm, ReviewForm

# Create your views here.

def index(request):
    # The home page for CrazyBookClub.
    return render(request, 'CrazyBookClub/index.html')

@login_required
def books(request):
    # Show all books.
    books = Book.objects.filter(owner=request.user).order_by('date_added')
    context = {'books': books}
    return render(request, 'CrazyBookClub/books.html', context)

@login_required
def book(request, book_id):
    # Show a single book and all its entries.
    book = Book.objects.get(id=book_id)
    # Make sure the book belongs to the current user.
    if book.owner != request.user:
        raise Http404
    
    entries = book.review_set.order_by('-date_added')
    context = {'book': book, 'entries': entries}
    return render(request, 'CrazyBookClub/book.html', context)

@login_required
def new_book(request):
    # Add a new book.
    if request.method != 'POST':
        # No data submitte; create a blank form.
        form = BookForm()
    else:
        # POST data submitted; process data.
        form = BookForm(data=request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.owner = request.user
            new_book.save()
            return redirect('CrazyBookClub:books')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'CrazyBookClub/new_book.html', context)

@login_required
def new_review(request, book_id):
    # Add a new review for a particular book.
    book = Book.objects.get(id=book_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ReviewForm()
    else:
        # POST data submitted; process data.
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.book = book
            new_review.save()
            return redirect('CrazyBookClub:book', book_id=book_id)
        
    # Display a blank or invalid form.
    context = {'book': book, 'form': form}
    return render(request, 'CrazyBookClub/new_review.html', context)

def edit_review(request, review_id):
    # Edit an existing review.
    review = Review.objects.get(id=review_id)
    book = review.book

    # Make sure that the review belongs to the user who wrote it.
    if book.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; pre-fill form with the currrent review.
        form = ReviewForm(instance=review)
    else:
        # POST data submitted, process data.
        form = ReviewForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('CrazyBookClub:book', book_id=book.id)
    
    context = {'review': review, 'book': book, 'form': form}
    return render(request, 'CrazyBookClub/edit_review.html', context)