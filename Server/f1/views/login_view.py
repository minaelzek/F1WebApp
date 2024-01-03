from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate, login, logout
from drf_spectacular.utils import extend_schema
from ..serializers.user_serializer import UserSerializer, LoginUserSerializer


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
