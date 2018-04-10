from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from .serializers import UserSocialSerializer

from rest_framework_jwt.views import jwt_response_payload_handler


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
        print(user)
        token = self.create_token(user)
        response_data = jwt_response_payload_handler(token, user, request)
        response = Response(response_data)

        return response
