from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.settings import api_settings

from .serializers import (
    UserSocialSerializer, UserSerializer, UserInfoSerializer,
    UserImageSerializer,
)

from rest_framework_jwt.views import ObtainJSONWebToken, jwt_response_payload_handler


class UserSocialLoginView(GenericAPIView):
    # 소셜 로그인 API
    permission_classes = [AllowAny]
    serializer_class = UserSocialSerializer

    def create_token(self, user):
        # 비밀번호가 없는 소셜 유저에 대한 인증 토큰 발급
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_hanlder = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_hanlder(payload)
        return token

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = self.create_token(user)
        response_data = jwt_response_payload_handler(token, user, request)
        response = Response(response_data)

        return response


class UserLoginView(ObtainJSONWebToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)

            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    lookup_field = 'uuid'


class UserInfoView(UpdateAPIView):
    serializer_class = UserInfoSerializer

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserImageView(UpdateAPIView):
    serializer_class = UserImageSerializer

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
