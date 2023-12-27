from django.contrib.auth.models import AbstractUser
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField("Created On", auto_now_add=True)
    updated_on = models.DateTimeField("Updated On", auto_now=True)
    
    class Meta:
        abstract = True


'''
F1APP User Models
'''
class User(AbstractUser):
    test = models.BooleanField(default=False)
    

# league configs ties to users
class League(BaseModel):
    pass


'''
F1 Specific Data
'''
class Team(BaseModel):
    name = models.CharField(max_length=200, blank=False, null=False)
    points = models.IntegerField(default=0)
    # points 

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

class QualifiyingResults(BaseModel):
    pass

class Circuit(BaseModel):
    name = models.CharField(max_length=200, blank=False, null=False)
    # TODO: number of laps
    # track length
    # Sector 1, 2, 3
    # DRS zones
    def __str__(self):
        return self.name

class RaceResult(BaseModel):
    circuit = models.OneToOneField(Circuit, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.season.year} {self.circuit.name}"

class RaceResultDriver(BaseModel):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    position = models.IntegerField(default=0, null=False, unique=False)
    race = models.ForeignKey(RaceResult, on_delete=models.CASCADE)
    did_not_finish = models.BooleanField(default=False)
    # only get fastest lap points if in top 10
    fastest_lap = models.BooleanField(default=False)
    driver_of_the_day = models.BooleanField(default=False)
    laps = models.IntegerField(default=0, null=False)
    # Race Time in miliseconds
    time = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.driver.name

    @property
    def driver_points(self):
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
    
    @property
    def team_points(self):
        pass

# this can probaly just be derived from driver results, based on team drivers and their positions 
# class RaceResultTeam(BaseModel):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
#     @property
#     def points(self):
#         pass