from django.urls import path
from .views import InfoUsineGetCreate, InfoUsineUpdateDelete

urlpatterns = [
    path('', InfoUsineGetCreate.as_view()),
    path('<int:pk>', InfoUsineUpdateDelete.as_view())
]