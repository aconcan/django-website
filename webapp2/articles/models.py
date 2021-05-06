from django.db import models

# Inheriting from models.Model
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # Add thumbnail and author later

def __str__(self):
    return self.title