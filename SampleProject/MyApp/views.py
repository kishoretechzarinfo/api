
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
# Create your views here.
@api_view(["POST"])
def sum(request):
    try:
        data=json.loads(request.body)
        num1 = int(data['number1'])
        num2 = int(data['number2'])
        #weight=str(height*10)
        sum = int(num1+num2)
        return JsonResponse({'result': sum,})
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
