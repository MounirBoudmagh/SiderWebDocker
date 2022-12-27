from .serializers import VideosSerializer
from rest_framework import generics
from .models import Video

# Create your views here.

class VideosGetCreate(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideosSerializer

class VideosUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideosSerializer