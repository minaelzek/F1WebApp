from rest_framework import serializers
from ..models.fantasy import League
from ..models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'