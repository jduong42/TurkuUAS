from django.db import models

# Create your models here.

class Game(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        # Returns a string presentation of the model.

        return self.name

class AddGame(models.Model):
    # Add a game to the platform

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'games'

    def __str__(self):
        # Returns a string representating the addition of the game.

        return f"{self.text[:50]}..."

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