from django.shortcuts import render
from .serializers import InfoUsineSerializer
from rest_framework import generics
from .models import InfoUsine

# Create your views here.

class InfoUsineGetCreate(generics.ListCreateAPIView):
    queryset = InfoUsine.objects.all()
    serializer_class = InfoUsineSerializer

class InfoUsineUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = InfoUsine.objects.all()
    serializer_class = InfoUsineSerializer