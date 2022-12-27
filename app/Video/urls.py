from django.urls import path
from .views import VideosGetCreate, VideosUpdateDelete

urlpatterns = [
    path('', VideosGetCreate.as_view()),
    path('<int:pk>', VideosUpdateDelete.as_view())
]