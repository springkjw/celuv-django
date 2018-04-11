from rest_framework import serializers

from apps.entertainments.models import Entertainment


class EntertainmentSerializer(serializers.ModelSerializer):
    # 기획사 직렬롸
    class Meta:
        model = Entertainment
        fields = [
            'id',
            'name',
        ]