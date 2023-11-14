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
]