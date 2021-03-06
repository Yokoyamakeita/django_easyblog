from pyexpat import model
from turtle import title
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

category=(('business','ビジネス'),('life','生活'),('other','その他'))

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=50,
        choices=category
    )
    def __str__(self):
        return self.title