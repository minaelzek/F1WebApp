from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from ..models.user import User
from ..models.fantasy import League
from ..serlializers.user_serlializer import UserSerializer
from ..serlializers.user_serlializer import UserLeagueSerializer

class UserListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserLeagues(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get (self, request):
        leagues = League.objects.filter(Q(owner__id=request.user.id) | Q(players__id=request.user.id))
        serializer = UserLeagueSerializer(leagues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = {
            'name': request.data.get('name'),
            'owner': request.user.id
        }
        serializer = UserLeagueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        league = get_object_or_404(League, pk=request.data.get('league_id'), owner=request.user)
        data = {
            'name': request.data.get('name', league.name)
        }
        player_ids_to_add = request.data.get('players', [])
        league.players.add(*player_ids_to_add)
        serializer = UserLeagueSerializer(instance=league, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)