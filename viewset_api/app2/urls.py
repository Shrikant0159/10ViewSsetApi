from rest_framework import routers
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .models import MovieModel


 
# import everything from views
from .views import *
  
# define the router
router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),

]