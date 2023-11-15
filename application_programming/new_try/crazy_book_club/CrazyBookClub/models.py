from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    # A book that user is reading.

    book = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Return a string representation of the book.
        return self.book
    
class Review(models.Model):
    # A review of the book
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    my_review = models.TextField(max_length=5000)
    stars = models.IntegerField
    #unfinished = models.BooleanField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'reviews'

    def __str__(self):
        # Return a string represntation of the review.
        return f"{self.my_review[:50]}..."