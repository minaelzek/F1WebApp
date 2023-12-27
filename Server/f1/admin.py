from django.contrib import admin
from .models.user import User
from .models.f1 import Team, Driver, Season, Circuit
from .models.f1_weekend import RaceResult, RaceResultDriver

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(Season)
admin.site.register(Circuit)
admin.site.register(RaceResult)

@admin.register(RaceResultDriver)
class RaceDriverPositionsAdmin(admin.ModelAdmin):
    list_filter = ["race"]
    list_display=("race" ,"driver_name", "position", "driver_points",)
    # fields=["driver"]

    def driver_name(self, obj):
        return obj.driver.name
