# Defines URL patterns for CrazyBookClub.

from django.urls import path

from . import views

app_name = 'CrazyBookClub'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all books.
    path('books/', views.books, name='books'),
    # Detail page for a single book entry.
    path('books/<int:book_id>/', views.book, name='book'),
    # Page for adding a new topic.
    path('new_book/', views.new_book, name='new_book'),
    # Page for adding new review.
    path('new_review/<int:book_id>/', views.new_review, name='new_review'),
]