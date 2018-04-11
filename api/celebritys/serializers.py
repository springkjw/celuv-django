from rest_framework import serializers

from apps.celebritys.models import Celebrity
from api.entertainments.serializers import EntertainmentSerializer

class CelebritySerializer(serializers.ModelSerializer):
    # 연예인 직렬화
    class Meta:
        model = Celebrity
        fields = [
            'id',
            'name',
            'image',
        ]


class CelebrityListSerializer(serializers.ModelSerializer):
    # 연예인 리스트 직렬화
    entertainment = EntertainmentSerializer(many=True)
    likes = serializers.SerializerMethodField()
    is_like = serializers.SerializerMethodField()

    class Meta:
        model = Celebrity
        fields = [
            'id',
            'name',
            'image',
            'entertainment',
            'likes',
            'is_like',
        ]

    def get_likes(self, obj):
        return obj.likes.count()

    def get_is_like(self, obj):
        return self.context['request'].user in obj.likes.all()