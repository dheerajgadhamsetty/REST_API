
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework import response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
class EmployeeList(APIView):
    def get(self, request):
        #qs = Employee.objects.all()
        qs = get_list_or_404(Employee)
        sobj = EmployeeSerializer(qs, many=True)
        return Response(sobj.data)
    
    # to store an object
    def post(self, request):
        sobj = EmployeeSerializer(data = request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sobj.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeModify(APIView):
    def get_object(self, id):
        try:
             return Employee.objects.get(id=id)
        except Employee.DoesNotExit:
            return Response({"error": "Given Employee object not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        obj = self.get_object(id)
        sobj = EmployeeSerializer(obj)
        return Response(sobj.data)

    def put(self, request, id):
        obj = self.get_object(id)
        sobj = EmployeeSerializer(obj, data = request.data)
        if sobj.is_valid():
            sobj.save()
            return Response(sobj.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sobj.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        obj = self.get_object(id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




