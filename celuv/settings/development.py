import os
from django.conf import settings

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}

# 정적 파일 설정
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(settings.BASE_DIR, 'static', 'app'),
]
STATIC_ROOT = os.path.join(settings.BASE_DIR, 'assets')
# 미디어 파일 설정
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')

RAVEN_CONFIG = {
    'dsn': 'https://d6a09e8ec10c4af082e92a5224205c5a:e956906083884767bd1ff79d81dc61e8@sentry.io/1191144',
}