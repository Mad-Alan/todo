from django.db import models

# Create your models here.

class ToDo (models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class library (models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=60)
    description = models.TextField(max_length=500)
    price = models.BigIntegerField(max_length=100)
    genre = models.CharField(max_length=15)
    author = models.CharField(max_length=20)
    year = models.DateTimeField(auto_now = False)
    date = models.DateTimeField(auto_now_add=True)