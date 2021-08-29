from myapp.serializers import ManagerSerializer
from myapp.models import Manager
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
class ManagerView(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
