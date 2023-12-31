from django.contrib import admin
from .models.user import User
from .models.f1 import Team, Driver, Season, Circuit
from .models.f1_weekend import RaceResult, RaceResultDriver
from .models.fantasy import League, ConstructorPrediction, WeekendEventPrediction, BonusWeekendPrediction, WeekendEventPredictionResult, BonusWeekendEventPredictionResult

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(Season)
admin.site.register(Circuit)
admin.site.register(RaceResult)
admin.site.register(League)
admin.site.register(ConstructorPrediction)
admin.site.register(WeekendEventPrediction)
admin.site.register(BonusWeekendPrediction)
admin.site.register(WeekendEventPredictionResult)
admin.site.register(BonusWeekendEventPredictionResult)

@admin.register(RaceResultDriver)
class RaceDriverPositionsAdmin(admin.ModelAdmin):
    list_filter = ["race"]
    list_display=("race" ,"driver_name", "position", "driver_points",)

    def driver_name(self, obj):
        return obj.driver.name
