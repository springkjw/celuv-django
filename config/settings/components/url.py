ROOT_URLCONF = 'config.urls'
LOGIN_URL = '/user/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/user/login'
LOGIN_EXEMPT_URLS = [
    r'^api/',
    r'^private',
    r'^user/login',
]

WSGI_APPLICATION = 'config.wsgi.application'