from rest_framework import serializers
from .models import Director, Movie

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    director_name = serializers.CharField(source='fk_director.name', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
