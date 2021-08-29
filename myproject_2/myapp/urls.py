from django.urls import path, include
from .import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('myapp', views.EmployeeView)
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',include(router.urls))
]