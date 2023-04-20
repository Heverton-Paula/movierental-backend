from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models

class User(AbstractUser):
    amount=models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    rented_movies=ArrayField(models.CharField(max_length=255), blank=True, default=list)
    pass
