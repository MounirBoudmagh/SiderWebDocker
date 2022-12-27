from django.shortcuts import render
from .serializers import JournalsSerializer
from rest_framework import generics
from .models import Journals

# Create your views here.

class JournalsGetCreate(generics.ListCreateAPIView):
    queryset = Journals.objects.all()
    serializer_class = JournalsSerializer

class JournalsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journals.objects.all()
    serializer_class = JournalsSerializer