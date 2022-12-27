from django.urls import path
from .views import ActualitieGetCreate, ActualitieUpdateDelete

urlpatterns = [
    path('', ActualitieGetCreate.as_view()),
    path('<int:pk>', ActualitieUpdateDelete.as_view())
]