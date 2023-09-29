from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from guests.serializers import GuestSerializer
from guests.models import Guest
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication



# Create your views here.
class GuestViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed only.
    User can not be edit via this APIs.
    """
    queryset = Guest.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    serializer_class = GuestSerializer

