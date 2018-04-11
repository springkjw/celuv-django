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
        return obj.like.count()

    def get_is_like(self, obj):
        return self.context['request'].user in obj.like.all()


class CelebrityLikeSerializer(serializers.ModelSerializer):
    is_like = serializers.BooleanField(required=True)

    class Meta:
        model = Celebrity
        fields = ('is_like',)

    def save(self, **kwargs):
        user = self.context['request'].user
        is_like = self.validated_data['is_like']
        instance = self.instance

        if is_like:
            instance.like.add(user)
        else:
            instance.like.remove(user)

        return instance
