from rest_framework import serializers
from .models import User

class F1UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'