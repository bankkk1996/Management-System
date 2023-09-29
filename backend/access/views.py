from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from users.serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class LoginView(APIView):
    
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user_tokens = Token.objects.filter(user=user)
            for token in user_tokens:
                token.delete()
            token, _ = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user)
            return Response({'token': token.key, 'user': serializer.data})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    authentication_classes = [SessionAuthentication]  # Use the appropriate authentication class
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logged out successfully'})