from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=False)
    director = models.CharField(max_length=100)
    duration = models.DurationField()
    price = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)