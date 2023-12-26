from django.contrib import admin
from .models import *

# class RaceDriverPositionsAdmin(admin.ModelAdmin):
#     model = RaceDriverPostions
#     fields = ('points',)

# Register your models here.
admin.site.register(User)

admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(Season)
admin.site.register(Circuit)
admin.site.register(RaceResult)
admin.site.register(RaceDriverPosition)
