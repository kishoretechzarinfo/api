
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Employeee.objects.all()
    serializer_class = serializers.EmployeeeSerializer
    