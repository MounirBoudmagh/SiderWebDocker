from django.shortcuts import render
from .serializers import ContactUsSerializer
from rest_framework import generics
from .models import Contact

# Create your views here.

class ContactUsGetCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactUsSerializer

class ContactUsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactUsSerializer