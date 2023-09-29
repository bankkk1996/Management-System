from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from technicians.serializers import TechnicianSerializer
from technicians.models import Technician
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication, TokenAuthentication


# Create your views here.
class TechnicianViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed only.
    User can not be edit via this APIs.
    """
    queryset = Technician.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    serializer_class = TechnicianSerializer

def index(request):
    return render(request,'index.html')