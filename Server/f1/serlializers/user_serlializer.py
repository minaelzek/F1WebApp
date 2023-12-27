from rest_framework import serializers
from ..models.user import User

class F1UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'