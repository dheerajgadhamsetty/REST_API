from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers 
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #fields = ('firstname', 'lastname')
        fields = '__all__'
        
