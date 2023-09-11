from .models import MovieModel

from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
			model = MovieModel
			fields = ('id','title', 'description')
