from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from .models import F1User
from .serializers import F1UserSerializer

class F1UserListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        users = F1User.objects.all()
        serializer = F1UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    