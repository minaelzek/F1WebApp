from django.contrib.auth.models import AbstractUser
from django.db import models

class F1User(AbstractUser):
    test = models.BooleanField(default=False)