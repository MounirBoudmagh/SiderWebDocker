from django.shortcuts import render
from .serializers import ActualitieSerializer
from rest_framework import generics
from .models import Actualitie

# Create your views here.

class ActualitieGetCreate(generics.ListCreateAPIView):
    queryset = Actualitie.objects.all()
    serializer_class = ActualitieSerializer

class ActualitieUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actualitie.objects.all()
    serializer_class = ActualitieSerializer