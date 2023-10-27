from django import forms

from .models import Book, Review

class BookForm(forms.ModelsForm):
    class Meta:
        model = Book
        fields = ['text']
        labels = {'text': ''}

class ReviewForm(forms.ModelsForm):
    class Meta:
        model = Review
        fields = ['text']
        labels = {'text': ''}
