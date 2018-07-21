from corsheaders.defaults import default_headers

# API CORS 설정
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = default_headers + (
    'csrftoken',
    'X_CSRF_TOKEN',
    'Cache-Control'
)