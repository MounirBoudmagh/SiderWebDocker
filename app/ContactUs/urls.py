from django.urls import path
from .views import ContactUsGetCreate, ContactUsUpdateDelete

urlpatterns = [
    path('', ContactUsGetCreate.as_view()),
    path('<int:pk>', ContactUsUpdateDelete.as_view())
]