from .base_model import BaseModel
from django.db import models

class Team(BaseModel):
    name = models.CharField(max_length=200, blank=False, null=False)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Driver(BaseModel):
    name = models.CharField(max_length=200, blank=False, null=False)
    points = models.IntegerField(default=0, null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Season(BaseModel):
    year = models.IntegerField(default=0, null=False)

    def __str__(self):
        return str(self.year)


class Circuit(BaseModel):
    name = models.CharField(max_length=200, blank=False, null=False)
    # TODO: number of laps
    # track length
    # Sector 1, 2, 3
    # DRS zones
    # country
    def __str__(self):
        return self.name
    