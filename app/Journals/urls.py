from django.urls import path
from .views import JournalsGetCreate, JournalsUpdateDelete

urlpatterns = [
    path('', JournalsGetCreate.as_view()),
    path('<int:pk>', JournalsUpdateDelete.as_view())
]