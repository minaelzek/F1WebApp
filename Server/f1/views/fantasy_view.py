from rest_framework import status, permissions, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from ..models.fantasy import ConstructorPrediction, WeekendEventPrediction
from ..serializers.fantasy_serializer import (
    ConstructorPredictionRequest,
    ConstructorPredictionResponse,
    WeekendEventPredictionRequest,
    WeekendEventPredictionResponse,
)


@extend_schema(
    request=ConstructorPredictionRequest,
    responses={201: ConstructorPredictionResponse, 400: None},
    tags=["Constructor Predictions"],
)
class ConstructorPredictionCreateView(generics.ListCreateAPIView):
    serializer_class = ConstructorPredictionRequest
    permission_classes = [permissions.IsAuthenticated]
    queryset = ConstructorPrediction.objects.all()

    def get_queryset(self):
        league_id = self.kwargs["league_id"]
        return ConstructorPrediction.objects.filter(user=self.request.user, league_id=league_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, league_id=self.kwargs["league_id"])

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ConstructorPredictionRequest
        elif self.request.method == 'GET':
            return ConstructorPredictionResponse


@extend_schema(
    request=ConstructorPredictionRequest,
    responses={200: ConstructorPredictionResponse, 400: None},
    tags=["Constructor Predictions"],
)
class ConstructorPredictionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConstructorPredictionResponse
    permission_classes = [permissions.IsAuthenticated]
    queryset = ConstructorPrediction.objects.all()
    lookup_url_kwarg = "prediction_id"

    def get_queryset(self):
        league_id = self.kwargs["league_id"]
        return ConstructorPrediction.objects.filter(league_id=league_id)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user, league_id=self.kwargs["league_id"])

    def get_serializer(self, *args, **kwargs):
        # mini hack to make PUTs partial updates
        kwargs["partial"] = True
        return super().get_serializer(*args, **kwargs)


@extend_schema(
    request=WeekendEventPredictionRequest,
    responses={200: WeekendEventPredictionResponse, 400: None},
    tags=["Weekend Predictions"],
)
class WeekendEventPredictionCreateView(generics.ListCreateAPIView):
    serializer_class = WeekendEventPredictionRequest
    permission_classes = [permissions.IsAuthenticated]
    queryset = ConstructorPrediction.objects.all()

    def get_queryset(self):
        league_id = self.kwargs["league_id"]
        return WeekendEventPrediction.objects.filter(user=self.request.user, league_id=league_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, league_id=self.kwargs["league_id"])

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WeekendEventPredictionRequest
        elif self.request.method == 'GET':
            return WeekendEventPredictionResponse


@extend_schema(
    request=WeekendEventPredictionRequest,
    responses={200: WeekendEventPredictionResponse, 400: None},
    tags=["Weekend Predictions"],
)
class WeekendEventPredictionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WeekendEventPredictionRequest
    permission_classes = [permissions.IsAuthenticated]
    queryset = WeekendEventPrediction.objects.all()
    lookup_url_kwarg = "prediction_id"

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WeekendEventPredictionResponse

    def get_queryset(self):
        league_id = self.kwargs["league_id"]
        return WeekendEventPrediction.objects.filter(league_id=league_id)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user, league_id=self.kwargs["league_id"])

    def get_serializer(self, *args, **kwargs):
        # mini hack to make PUTs partial updates
        kwargs["partial"] = True
        return super().get_serializer(*args, **kwargs)
