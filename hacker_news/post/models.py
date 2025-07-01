from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=1024)
    author_name = models.CharField(max_length=32)
    points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
