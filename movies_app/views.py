from django.shortcuts import render
from rest_framework import viewsets
from .models import Director, Movie
from .serializers import DirectorSerializer, MovieSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
