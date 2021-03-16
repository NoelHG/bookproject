from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    recommendationCount = models.IntegerField() #chosen over recommendation relation for query speed
