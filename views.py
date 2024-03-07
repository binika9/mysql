from django.http import JsonResponse
from django.shortcuts import render

from myapplication.models import Employees
from myapplication.serializers import EmployeeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def employee_list(request):
    employees = Employees.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse({'employees', serializer.data})