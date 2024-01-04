from rest_framework import generics
from ..models.f1 import Team, Driver, Season, Circuit
from ..serializers.f1_serializer import CircuitSerializer, DriverSerializer, SeasonSerializer, TeamSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    responses={200: TeamSerializer, 400: None},
    tags=["F1"],
)
class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

@extend_schema(
    responses={200: DriverSerializer, 400: None},
    tags=["F1"],
)
class DriverListView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

@extend_schema(
    responses={200: SeasonSerializer, 400: None},
    tags=["F1"],
)
class SeasonListView(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

@extend_schema(
    responses={200: CircuitSerializer, 400: None},
    tags=["F1"],
)
class CircuitListView(generics.ListAPIView):
    queryset = Circuit.objects.all()
    serializer_class = CircuitSerializer
