from rest_framework import serializers
from .models import Journals

class JournalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journals
        fields = '__all__'