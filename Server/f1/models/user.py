from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    #keeping this for testing purposes, will remove after
    REQUIRED_FIELDS = []
