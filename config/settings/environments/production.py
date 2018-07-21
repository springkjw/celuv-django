DEBUG = False
ALLOWED_HOSTS = ['*']

AWS_STORAGE_BUCKET_NAME = 'celuv-test'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# 정적 파일 설정
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'app'),
)

# 미디어 파일 설정
MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN