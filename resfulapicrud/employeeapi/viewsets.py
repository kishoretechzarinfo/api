
from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employeee.objects.all()
    serializer_class = serializers.EmployeeeSerializer
    