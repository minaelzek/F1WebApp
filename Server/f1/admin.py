from django.contrib import admin
from .models import *

@admin.register(RaceResultDriver)
class RaceDriverPositionsAdmin(admin.ModelAdmin):
    list_display=("race" ,"driver_name", "position", "points")
    # fields=["driver"]

    # def race_name(self, obj):
    #     return obj.race.name

    def driver_name(self, obj):
        return obj.driver.name
    

# Register your models here.
admin.site.register(User)

admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(Season)
admin.site.register(Circuit)
admin.site.register(RaceResult)
# admin.site.register(RaceResultDriver)
# admin.site.register(RaceResultTeam)
