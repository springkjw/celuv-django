from rest_framework import serializers

from apps.celebritys.models import Celebrity


class CelebritySerializer(serializers.ModelSerializer):
    # 연예인 직렬화
    class Meta:
        model = Celebrity
        fields = [
            'id',
            'name',
            'image',
        ]
