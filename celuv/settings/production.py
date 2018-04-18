import os
import raven
from django.conf import settings

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'celuv',
        'USER': 'entresong',
        'PASSWORD': 'musicsul057',
        'HOST': 'celuv.cm4njigt3uj7.ap-northeast-2.rds.amazonaws.com'
    }
}

AWS_STORAGE_BUCKET_NAME = 'celuv-test'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# 정적 파일 설정
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_DIRS = (
    os.path.join(settings.BASE_DIR, 'static', 'app'),
)

# 미디어 파일 설정
MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN

# Sentry 설정
RAVEN_CONFIG = {
    'dsn': 'https://d6a09e8ec10c4af082e92a5224205c5a:e956906083884767bd1ff79d81dc61e8@sentry.io/1191144',
}
