from rest_framework import serializers
from ..models.fantasy import League
from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = "__all__"
