from django.db import models
from .base_model import BaseModel
from .user import User
from .f1 import Season, Circuit, Driver, Team
from .f1_weekend import RaceResult

class League(BaseModel):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    players = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    
class ConstructorPrediction(BaseModel):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team_1 = models.ForeignKey(Team, related_name="team_1", on_delete=models.CASCADE)
    team_2 = models.ForeignKey(Team, related_name="team_2", on_delete=models.CASCADE)
    team_3 = models.ForeignKey(Team, related_name="team_3", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}-{self.league.name}"

class WeekendEventPrediction(BaseModel):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.ForeignKey(RaceResult, on_delete=models.CASCADE)
    podium_1 = models.ForeignKey(Driver, related_name="podium_1", on_delete=models.CASCADE)
    podium_2 = models.ForeignKey(Driver, related_name="podium_2", on_delete=models.CASCADE)
    podium_3 = models.ForeignKey(Driver, related_name="podium_3", on_delete=models.CASCADE)
    driver_4 = models.ForeignKey(Driver, related_name="driver_4", on_delete=models.CASCADE)
    driver_5 = models.ForeignKey(Driver, related_name="driver_5", on_delete=models.CASCADE)
    fastest_lap = models.ForeignKey(Driver, related_name="fastest_lap", on_delete=models.CASCADE)
    driver_of_the_day = models.ForeignKey(Driver, related_name="driver_of_the_day", on_delete=models.CASCADE) # TODO: remove?
    
    def __str__(self):
        return f"{self.user.username}-{self.league.name}: {self.league.season.year} {self.circuit.name}"
    
# TODO: This is subject to change
# TODO: add model for side bet (add points and description)
class BonusWeekendPrediction(BaseModel):
    weekend_event_prediction = models.ForeignKey(WeekendEventPrediction, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, null=True, on_delete=models.CASCADE)
    # where false is under and true is over
    prediction = models.BooleanField(null=True)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.weekend_event_prediction

class WeekendEventPredictionResult(BaseModel):
    weekend_event_prediction = models.ForeignKey(WeekendEventPrediction, on_delete=models.CASCADE)
    fantasy_points_gained = models.PositiveIntegerField(default=0, null=False)

class BonusWeekendEventPredictionResult(BaseModel):
    bonus_weekend_prediction = models.ForeignKey(BonusWeekendPrediction, on_delete=models.CASCADE)
    fantasy_points_gained = models.PositiveIntegerField(default=0, null=False)

# TODO: a config model that will weigth each prediction? (podiums, correct top5, dotd, fl)

