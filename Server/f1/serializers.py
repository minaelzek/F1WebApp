from rest_framework import serializers
from .models import F1User

class F1UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = F1User
        fields = '__all__'