from django import forms

from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book']
        labels = {'book': ''}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book']
        labels = {'book': ''}
        widgets = {'book': forms.Textarea(attrs={'cols': 80})}
        