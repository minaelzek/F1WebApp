from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate, login, logout
from drf_spectacular.utils import extend_schema
from ..serializers.user_serializer import UserSerializer, LoginUserSerializer
from ..serializers.login_summary_serializer import LoginSummarySerializer
from ..models.f1 import Team, Driver
from ..models.fantasy import League
from ..models.user import User


class RegisterUserView(APIView):
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        request=UserSerializer,
        responses={201: UserSerializer, 400: None},
        tags=["User"],
    )
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

    @extend_schema(
        request=LoginUserSerializer, responses={200: None, 401: None}, tags=["User"]
    )
    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=request.data.get("username"),
                password=request.data.get("password"),
            )
            if user:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                res = {"error": "Invalid Username and Passward Combination"}
                return Response(res, status=status.HTTP_401_UNAUTHORIZED)


class LogoutUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    # TODO: need to add extend_schema to this
    @extend_schema(request=None, responses=None, tags=["User"])
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

@extend_schema(request= None, responses=LoginSummarySerializer, tags=["User"])
class LoginSummaryView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LoginSummarySerializer

    def get_object(self):
        user_id = self.request.user.id
        user_instance = generics.get_object_or_404(User, pk=user_id)
        
        teams_queryset = Team.objects.all()
        drivers_queryset = Driver.objects.all()
        leagues_queryset = League.objects.filter(players__id=user_id)

        return {
            'user': user_instance,
            'teams': teams_queryset,
            'drivers': drivers_queryset,
            'leagues': leagues_queryset
        }

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)