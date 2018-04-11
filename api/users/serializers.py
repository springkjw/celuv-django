import hashlib
import random

from rest_framework import serializers
from apps.users.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    # 유저 직렬화
    profile_image = serializers.SerializerMethodField()
    is_staff = serializers.SerializerMethodField()
    is_social = serializers.SerializerMethodField()
    personal_info = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = [
            'uuid',
            'email',
            'is_staff',
            'is_social',
            'is_active',
            'personal_info',
            'profile_image',
        ]

    def get_profile_image(self, obj):
        if obj.image:
            return obj.image
        return None

    def get_is_staff(self, obj):
        return obj.is_staff

    def get_is_social(self, obj):
        if obj.provider != 'c':
            return True
        return False

    def get_personal_info(self, obj):
        return {
            'name': obj.name,
            'sex': obj.sex,
            'birth': obj.birth,
        }



class UserSocialSerializer(serializers.ModelSerializer):
    # 소셜 로그인 유저에 대한 직렬화
    class Meta:
        model = MyUser
        fields = [
            'provider',
            'uid'
        ]

    def generate_random_email(self):
        while True:
            _random = hashlib.sha256(
                str(random.random()).encode('utf-8')).hexdigest()[:10]
            email = '%s@celuv.xyz' % _random
            if not MyUser.objects.filter(email=email).exists():
                break
        return email

    def save(self, **kwargs):
        provider = self.validated_data['provider']
        uid = self.validated_data['uid']

        user = MyUser.objects.filter(
            provider=provider, uid=uid
        )
        if not user.exists():
            email = self.generate_random_email()
            new_user = MyUser.objects.create(
                email=email,
                **self.validated_data
            )
            return new_user
        return user.first()
