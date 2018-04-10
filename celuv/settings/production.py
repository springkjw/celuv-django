import os
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
AWS_REGION = 'ap-northeast-2'
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_S3_ACCESS_KEY_ID = 'AKIAIAMY5ESYHE5QC4NQ'
AWS_S3_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'celuv'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# 정적 파일 설정
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# 미디어 파일 설정
MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')
