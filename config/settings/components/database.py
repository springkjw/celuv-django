DATABASES = {
    'default': {}    
}

if ENV == 'development':
    DATABASES['default'].update({
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'celuv',
        'USER': 'entresong',
        'PASSWORD': 'musicsul057',
        'HOST': 'celuv.cm4njigt3uj7.ap-northeast-2.rds.amazonaws.com'
    })
else:
    DATABASES['default'].update({
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'celuv',
        'USER': 'entresong',
        'PASSWORD': 'musicsul057',
        'HOST': 'celuv.cm4njigt3uj7.ap-northeast-2.rds.amazonaws.com'
    })
    