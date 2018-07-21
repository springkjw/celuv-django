DEBUG = True
ALLOWED_HOSTS = ['*']

# 정적 파일 설정
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static', 'app'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
# 미디어 파일 설정
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')