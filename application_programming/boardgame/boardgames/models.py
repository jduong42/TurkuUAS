from django.db import models

# Create your models here.

class Game(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        # Returns a string presentation of the model.

        return self.name

class User(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        # Returns a string presentation of the model.

        return self.name

class Loan(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)