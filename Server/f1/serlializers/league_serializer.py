from rest_framework import serializers
from ..models.fantasy import League

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'