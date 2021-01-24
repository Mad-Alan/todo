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
    description = models.TextField()
    price = models.IntegerField()
    genre = models.CharField(max_length=30)
    author = models.CharField(max_length=100)
    year = models.DateField()
    is_favorite = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)