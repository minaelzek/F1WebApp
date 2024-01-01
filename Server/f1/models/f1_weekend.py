from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from .base_model import BaseModel
from .f1 import Driver, Circuit, Season

'''
Base Models for weekend events
'''
class BaseModelEventResult(BaseModel):
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    date = models.DateField(null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.season.year} {self.circuit.name}"

class BaseModelEventDriverResult(BaseModel):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    position = models.IntegerField(default=0, null=False, unique=False, validators=([MinValueValidator(1), MaxValueValidator(25)]))
    did_not_finish = models.BooleanField(default=False)
    laps = models.IntegerField(default=0, null=False)
    # Race Time in miliseconds
    time = models.IntegerField(default=0, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.driver.name

'''
Sprint Shootout
'''
class SprintShootoutResult(BaseModelEventResult):
    pass

class SprintShootoutResultDriver(BaseModel):
    pass

'''
Sprint
'''
class SprintResult(BaseModelEventResult):
    pass

class SprintResultDriver(BaseModel):
    pass
    
'''
Qualifying
'''
class QualifiyingResults(BaseModelEventResult):
    pass

class QualifyingResultDriver(BaseModelEventDriverResult):
    qualifying = models.ForeignKey(QualifiyingResults, on_delete=models.CASCADE)
    
'''
Race
'''
class RaceResult(BaseModelEventResult):
    pass

class RaceResultDriver(BaseModelEventDriverResult):
    race = models.ForeignKey(RaceResult, on_delete=models.CASCADE)
    # TODO: only get fastest lap points if in top 10
    fastest_lap = models.BooleanField(default=False)
    driver_of_the_day = models.BooleanField(default=False)

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
        if(self.position in position_to_points):
            points += position_to_points[self.position]
        return points
    
    @property
    def team_points(self):
        pass
