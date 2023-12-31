from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from ..models.user import User
from ..models.fantasy import League
from ..serlializers.user_serlializer import UserSerializer, UserLeagueSerializer


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=None, responses={200: UserSerializer}, tags=["User"])
    def get(self, request):
        # TODO
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # TODO: PUT, PATCH, DELETE(this will just set account to inactive)


class UserCreateLeague(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=UserLeagueSerializer,
        responses={201: UserLeagueSerializer, 400: None},
        tags=["League"],
    )
    def post(self, request):
        data = {
            "name": request.data.get("name"),
            "owner": request.user.id,
            "season": request.data.get("season"),
            "players": request.data.get("players"),
        }
        serializer = UserLeagueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLeague(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=None, responses={200: UserSerializer}, tags=["League"])
    def get(self, request, league_id):
        leagues = League.objects.filter(pk=league_id, players__id=request.user.id)
        serializer = UserLeagueSerializer(leagues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=UserLeagueSerializer,
        responses={200: UserLeagueSerializer, 400: None},
        tags=["League"],
    )
    def patch(self, request, league_id):
        league = get_object_or_404(League, pk=league_id, owner=request.user.id)
        data = {"name": request.data.get("name", league.name)}
        player_ids_to_add = request.data.get("players", [])
        league.players.add(*player_ids_to_add)
        serializer = UserLeagueSerializer(instance=league, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=UserLeagueSerializer, responses=None, tags=["League"])
    def delete(self, request, league_id):
        league = get_object_or_404(League, pk=league_id, owner=request.user.id)
        league.delete()
        return Response(status=status.HTTP_200_OK)


class UserLeagues(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=None, responses={200: UserSerializer}, tags=["League"])
    def get(self, request):
        leagues = League.objects.filter(players__id=request.user.id)
        serializer = UserLeagueSerializer(leagues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
