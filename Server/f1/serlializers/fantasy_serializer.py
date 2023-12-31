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


class WeekendEventPredictionRequest(serializers.ModelSerializer):
    class Meta:
        model = WeekendEventPrediction
        fields = [
            "circuit",
            "podium_1",
            "podium_2",
            "podium_3",
            "driver_4",
            "driver_5",
            "fastest_lap",
            "driver_of_the_day",
        ]


class WeekendEventPredictionResponse(serializers.ModelSerializer):
    class Meta:
        model = WeekendEventPrediction
        fields = [
            "id",
            "league",
            "user",
            "circuit",
            "podium_1",
            "podium_2",
            "podium_3",
            "driver_4",
            "driver_5",
            "fastest_lap",
            "driver_of_the_day",
        ]


class WeekendEventPredictionResult(serializers.ModelSerializer):
    class Meta:
        model = WeekendEventPredictionResult
        fields = "__all__"
