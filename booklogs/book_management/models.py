from django.db import models

# Book class for the book catalog
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=50)