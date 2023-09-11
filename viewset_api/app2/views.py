from rest_framework import viewsets

from django.shortcuts import render
from . serializers import MovieSerializer
from .models import MovieModel

# create a viewset
class MovieViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = MovieModel.objects.all()
	
	# specify serializer to be used
	serializer_class = MovieSerializer