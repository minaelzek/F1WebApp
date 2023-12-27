from django.contrib.auth.models import AbstractUser
from django.db import models

'''
F1APP User Models
'''
class User(AbstractUser):
    test = models.BooleanField(default=False)

# league configs ties to users
class League(models.Model):
    pass


'''
F1 Specific Data
'''
class Team(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    points = models.IntegerField(default=0)
    # points 

class Driver(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    points = models.IntegerField(default=0, null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Season(models.Model):
    year = models.IntegerField(default=0, null=False)

class QualifiyingResults(models.Model):
    pass

class Circuit(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    # TODO: number of laps
    # track length
    # Sector 1, 2, 3
    # DRS zones

class RaceResult(models.Model):
    circuit = models.OneToOneField(Circuit, on_delete=models.CASCADE)
    season = models.OneToOneField(Season, on_delete=models.CASCADE)

class RaceResultDriver(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    position = models.IntegerField(default=0, null=False, unique=True)
    race = models.ForeignKey(RaceResult, on_delete=models.CASCADE)
    did_not_finish = models.BooleanField(default=False)
    # only get fastest lap points if in top 10
    fastest_lap = models.BooleanField(default=False)
    driver_of_the_day = models.BooleanField(default=False)
    laps = models.IntegerField(default=0, null=False)
    # Race Time in miliseconds
    time = models.IntegerField(default=0, null=False)

    @property
    def points(self):
        position_to_points = {
            1: 25,
            2: 18,
            3: 15,
            4: 12, 
            5: 10,
            6: 8,
            7: 6,
            8: 4,
            9: 2,
            10: 1
        }

        points = 0
        if(self.fastest_lap and self.position >= 10):
            points += 1
        if(position_to_points[self.position]):
            points += position_to_points[self.position]
        return points
    
    def get_driver_name(self):
        return self.driver.name

# this can probaly just be derived from driver results, based on team drivers and their positions 
class RaceResultTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    @property
    def points(self):
        pass