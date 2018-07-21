import os
from django.conf import settings

from rest_framework_jwt.utils import jwt_decode_handler
from storages.backends.s3boto3 import S3Boto3Storage

from api.users.serializers import UserSerializer


def StaticRootS3BotoStorage(): return S3Boto3Storage(location='static')


def MediaRootS3BotoStorage(): return S3Boto3Storage(location='media')


os.environ['S3_USE_SIGV4'] = 'True'


class S3Storage(S3Boto3Storage):
    @property
    def connection(self):
        if self._connection is None:
            self._connection = self.connection_class(
                self.access_key, self.secret_key,
                calling_format=self.calling_format,
                host='s3.%s.amazonaws.com' % settings.S3DIRECT_REGION
            )
        return self._connection


def jwt_response_payload_handler(token, user=None, request=None):
    decode = jwt_decode_handler(token)
    response_data = {
        'payload': {
            'token': token,
            'orig_iat': decode['orig_iat'],
            'exp': decode['exp']
        },
        'user': UserSerializer(user, context={'request': request}).data
    }

    return response_data
