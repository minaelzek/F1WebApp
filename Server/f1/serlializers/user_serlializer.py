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


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(trim_whitespace=True)
    password = serializers.CharField(write_only=True)


class UserLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = "__all__"
