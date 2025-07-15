from django.db import models


# Create your models here.

class ShortURL(models.Model):
    code = models.CharField(max_length=8, unique=True)
    original_url = models.URLField(max_length=200)
    access_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        app_label = "shortener"
        db_table = "short_url"