from django.http  import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
# function based view
def myform(request):
    return render(request,"myform.html")

# class based view 

class Addition(APIView):
    def post(self, request):
        x = float(request.data.get("firstnum"))
        y = float(request.data.get("secondnum"))
        z = x+y
        str = "addition of %.2f and %.2f is %.2f" % (x,y,z)
        return HttpResponse(str)



