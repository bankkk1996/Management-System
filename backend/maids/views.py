from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from maids.serializers import MaidSerializer
from maids.models import Maid
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication


# Create your views here.
class MaidViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed only.
    User can not be edit via this APIs.
    """
    queryset = Maid.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    serializer_class = MaidSerializer