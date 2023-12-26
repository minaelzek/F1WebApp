from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    test = models.BooleanField(default=False)

# TODO: make base model
class Team(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    points = models.IntegerField(default=0)

class Driver(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    points = models.IntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


