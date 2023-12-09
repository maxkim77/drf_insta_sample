from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank = True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    