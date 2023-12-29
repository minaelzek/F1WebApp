from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from django.db.models import Q
from ..models.user import User
from ..models.fantasy import League
from ..serlializers.user_serlializer import UserSerializer
from ..serlializers.league_serializer import LeagueSerializer

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
        serializer = LeagueSerializer(leagues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
