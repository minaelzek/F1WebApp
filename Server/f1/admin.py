from django.contrib import admin
from .models import *

@admin.register(RaceResultDriver)
class RaceDriverPositionsAdmin(admin.ModelAdmin):
    list_display=("driver_name", "position", "points")

    def driver_name(self, obj):
        return obj.get_driver_name()

# Register your models here.
admin.site.register(User)

admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(Season)
admin.site.register(Circuit)
admin.site.register(RaceResult)
# admin.site.register(RaceResultDriver)
# admin.site.register(RaceResultTeam)
