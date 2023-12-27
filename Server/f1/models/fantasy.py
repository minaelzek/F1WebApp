from django.db import models
from .base_model import BaseModel
from .user import User
from .f1 import Season, Circuit, Driver

class League(BaseModel):
    name = models.CharField(max_length=200, blank=False, null=False)
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    players = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    
class ConstructorPrediction(BaseModel):
    pass

class WeekendEventPrediction(BaseModel):
    # league, user, season, circuit, podium_1, podium_2, podium_3, driver_4, driver_5 ,fastest_lap, driver_of_the_day, bonus_predictions(fk)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    podium_1 = models.ForeignKey(Driver, related_name="podium_1", on_delete=models.CASCADE)
    podium_2 = models.ForeignKey(Driver, related_name="podium_2", on_delete=models.CASCADE)
    podium_3 = models.ForeignKey(Driver, related_name="podium_3", on_delete=models.CASCADE)
    driver_4 = models.ForeignKey(Driver, related_name="driver_4", on_delete=models.CASCADE)
    driver_5 = models.ForeignKey(Driver, related_name="driver_5", on_delete=models.CASCADE)
    fastest_lap = models.ForeignKey(Driver, related_name="fastest_lap", on_delete=models.CASCADE)
    driver_of_the_day = models.ForeignKey(Driver, related_name="driver_of_the_day", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.name}-{self.league.name}: {self.season.name} {self.circuit.name}"
    
class BonusWeekendPrediction(BaseModel):
    # league, user, over, under, description, prediction (whether over or under)
    weekend_event_prediction = models.ForeignKey(WeekendEventPrediction, on_delete=models.CASCADE)
    over = models.IntegerField(default=0, null=False)
    under = models.IntegerField(default=0, null=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.weekend_event_prediction

# These would get populated after the weekend events are all over
class WeekendEventPredictionResult(BaseModel):
    # WeekendEventPrediction, points_gained
    pass

class BonusWeekendEventPredictionResult(BaseModel):
    # BonusWeekendPrediction, points_gained
    pass

# TODO: a config model that will weigth each prediction? (podiums, correct top5, dotd, fl)

