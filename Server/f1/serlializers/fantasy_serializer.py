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

    def validate(self, data):
        team_1 = data.get('team_1')
        team_2 = data.get('team_2')
        team_3 = data.get('team_3')

        # Check that each team is unique
        if team_1 == team_2 or team_1 == team_3 or team_2 == team_3:
            raise serializers.ValidationError("Teams must be unique.")

        return data


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

def validate(self, data):
        driver_values = [
            data["podium_1"],
            data["podium_2"],
            data["podium_3"],
            data["driver_4"],
            data["driver_5"],
        ]

        if len(driver_values) != len(set(driver_values)):
            raise serializers.ValidationError("Driver values must be unique.")

        return data

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
