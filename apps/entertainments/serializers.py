from rest_framework import serializers

from .models import Entertainment


class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entertainment
        fields = [
            'name',
            'image',
            'start',
            'homepage',
            'code',
        ]