DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'storages',
    'rest_framework',
    'rest_framework_swagger',
    'django_select2',
    'push_notifications',
    'raven.contrib.django.raven_compat',
]
PROJECT_APPS = [
    'apps.bases',
    'apps.users',
    'apps.celebritys',
    'apps.schedules',
    'apps.entertainments',
    'apps.feedbacks',
    'apps.notifications',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS