
from django.urls import path,include
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register('myapp',views.ManagerView)  

urlpatterns = [
    path('', include(router.urls))
]