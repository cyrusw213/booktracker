from django.db import models
from django.urls import reverse
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

def __str__(self):
    return self.name

  # Add this method
def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})
