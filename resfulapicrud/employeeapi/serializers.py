from rest_framework import serializers
from .models import Employeee

class EmployeeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeee
        fields = '__all__'