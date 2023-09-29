from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from users.serializers import UserSerializer
from users.models import User


# Create your views here.
class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed only.
    User can not be edit via this APIs.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer