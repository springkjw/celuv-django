import os
from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


def StaticRootS3BotoStorage(): return S3BotoStorage(location='static')


def MediaRootS3BotoStorage(): return S3BotoStorage(location='media')


os.environ['S3_USE_SIGV4'] = 'True'


class S3Storage(S3BotoStorage):
    @property
    def connection(self):
        if self._connection is None:
            self._connection = self.connection_class(
                self.access_key, self.secret_key,
                calling_format=self.calling_format,
                host='s3.%s.amazonaws.com' % settings.S3DIRECT_REGION
            )
        return self._connection
