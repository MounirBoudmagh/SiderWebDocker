from rest_framework import serializers
from .models import InfoUsine

class InfoUsineSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoUsine
        fields = '__all__'