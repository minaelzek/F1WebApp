from rest_framework import serializers
from ..models.fantasy import (
    ConstructorPrediction,
    WeekendEventPrediction,
    WeekendEventPredictionResult,
)


class ConstructorPredictionSerlializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructorPrediction
        fields = "__all__"


class WeekendEventPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekendEventPrediction
        fields = "__all__"


class WeekendEventPredictionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekendEventPredictionResult
        fields = "__all__"
