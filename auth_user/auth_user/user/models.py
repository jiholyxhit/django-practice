from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    social_provider = models.CharField(max_length=8, null=True)
