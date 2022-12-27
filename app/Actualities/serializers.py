from rest_framework import serializers
from .models import Actualitie

class ActualitieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actualitie
        fields = '__all__'