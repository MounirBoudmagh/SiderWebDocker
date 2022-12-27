from django.urls import path
from .views import *

urlpatterns = [
    path('images/', ImagesGetCreate.as_view()),
    path('images/<int:pk>/', ImagesUpdateDelete.as_view()),

    path('gallery/', GalleryGetCreate.as_view()),
    path('gallery/<int:pk>', GalleryUpdateDelete.as_view()),
]