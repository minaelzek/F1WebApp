from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    test = models.BooleanField(default=False)
    
