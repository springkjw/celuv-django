import os
from django.conf import settings

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}


AWS_ACCESS_KEY_ID = 'AKIAIGLOIDQAXXBEO7AA'
AWS_SECRET_ACCESS_KEY = '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'

AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'celuv.utils.MediaRootS31otoStorage'
STATICFILES_STORAGE = 'celuv.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'celuv'
S3DIRECT_REGION = 'ap-northeast-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = 'https://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL

STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

AWS_S3_HOST = 's3.%s.amazonaws.com' % S3DIRECT_REGION
