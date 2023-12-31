from rest_framework import status, permissions, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from ..models.fantasy import ConstructorPrediction
from ..serlializers.fantasy_serializer import (
    ConstructorPredictionRequest,
    ConstructorPredictionResponse,
)


@extend_schema(
    request=ConstructorPredictionRequest,
    responses={201: ConstructorPredictionResponse, 400: None},
    tags=["Constructor Predictions"],
)
class ConstructorPredictionCreateView(generics.CreateAPIView):
    serializer_class = ConstructorPredictionRequest
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, league_id=self.kwargs["league_id"])


@extend_schema(
    request=ConstructorPredictionRequest,
    responses={200: ConstructorPredictionResponse, 400: None},
    tags=["Constructor Predictions"],
)
class ConstructorPredictionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConstructorPredictionResponse
    permission_classes = [permissions.IsAuthenticated]
    queryset = ConstructorPrediction.objects.all()
    lookup_url_kwarg = 'prediction_id'

    def get_queryset(self):
        league_id = self.kwargs["league_id"]
        return ConstructorPrediction.objects.filter(league_id=league_id)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user, league_id=self.kwargs["league_id"])

    def get_serializer(self, *args, **kwargs):
        # mini hack to make PUTs partial updates 
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)