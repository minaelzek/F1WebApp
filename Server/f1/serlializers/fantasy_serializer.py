from rest_framework import serializers
from ..models.fantasy import (
    ConstructorPrediction,
    WeekendEventPrediction,
    WeekendEventPredictionResult,
)


class ConstructorPredictionRequest(serializers.ModelSerializer):
    class Meta:
        model = ConstructorPrediction
        fields = ["team_1", "team_2", "team_3"]


class ConstructorPredictionResponse(serializers.ModelSerializer):
    class Meta:
        model = ConstructorPrediction
        fields = ["id", "league", "user", "team_1", "team_2", "team_3"]


class WeekendEventPrediction(serializers.ModelSerializer):
    class Meta:
        model = WeekendEventPrediction
        fields = "__all__"


class WeekendEventPredictionResult(serializers.ModelSerializer):
    class Meta:
        model = WeekendEventPredictionResult
        fields = "__all__"
