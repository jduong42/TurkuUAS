# Definies URL patterns for CrazyBookClub

from django.urls import path

from . import views

app_name = 'CrazyBookClub'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page that shows all the books.
    path('books/', views.books, name='books'),

    # Page that shows all the reviews.
    path('reviews/', views.reviews, name='reviews')
]