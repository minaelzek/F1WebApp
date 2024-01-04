from rest_framework import serializers
from ..models.f1 import Team, Driver, Season, Circuit

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = "__all__"

class CircuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuit
        fields = "__all__"