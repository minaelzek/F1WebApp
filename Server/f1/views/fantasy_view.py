from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from ..models.fantasy import ConstructorPrediction
from ..serlializers.fantasy_serializer import ConstructorPredictionSerlializer


class ConstructorPredictionView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        request=None,
        responses={200: ConstructorPredictionSerlializer},
        tags=["Predictions"],
    )
    def get(self, request, user_id, prediction_id):
        constructor_prediction = ConstructorPrediction.objects.get(
            id=prediction_id, user__id=user_id
        )
        serializer = ConstructorPredictionSerlializer(constructor_prediction)
        return Response(serializer.data, status=status.HTTP_200_OK)
