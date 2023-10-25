from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    authors = models.JSONField()
    year_published = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    my_review = models.TextField(max_length=5000)
    stars = models.IntegerField()
    unfinished = models.BooleanField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.my_review[:50]}"