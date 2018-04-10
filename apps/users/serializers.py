from rest_framework import serializers

from .models import MyUser


class MyUserFanSerializer(serializers.ModelSerializer):
    sex = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = [
            'pk',
            'username',
            'image',
            'name',
            'email',
            'sex',
            'date_joined',
            'provider',
            'birth',
            'is_active',
        ]

    def get_sex(self, obj):
        return obj.get_sex_display()

    def get_provider(self, obj):
        return obj.get_provider_display()


class MyUserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'name',
            'email',
            'phone',
            'password',
        ]

    def create(Self, validated_data):
        user = super().create(validated_data)
        user.is_manager = True
        user.save()
        return user
