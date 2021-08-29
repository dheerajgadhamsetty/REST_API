from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.
class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer