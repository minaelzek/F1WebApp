from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from ..models.user import User
from ..models.fantasy import League
from ..serlializers.user_serlializer import UserSerializer
from ..serlializers.user_serlializer import UserLeagueSerializer
from ..serlializers.user_serlializer import LoginUserSerializer
from drf_spectacular.utils import extend_schema

class RegisterUserView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(request=UserSerializer, responses=None)
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data, many=False)
        if serializer.is_valid():
            user = serializer.create(serializer.data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUserView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [SessionAuthentication]

    @extend_schema(request=LoginUserSerializer, responses=None)
    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
            if user:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        
class LogoutUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=None, responses=UserSerializer)
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserLeagues(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=None, responses=UserSerializer)
    def get(self, request):
        leagues = League.objects.filter(players__id=request.user.id)
        serializer = UserLeagueSerializer(leagues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(request=UserLeagueSerializer, responses=None)
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
    
    @extend_schema(request=UserLeagueSerializer, responses=None)
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