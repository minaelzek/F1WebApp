from rest_framework import serializers
from ..models.f1 import Team, Driver
from ..models.user import User
from ..models.fantasy import League

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = "__all__"

class LoginSummarySerializer(serializers.Serializer):
    user = UserSerializer()
    teams = TeamSerializer(many=True)
    drivers = DriverSerializer(many=True)
    leagues = LeagueSerializer(many=True)