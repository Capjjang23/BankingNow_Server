from .base import *

# 작업하는 환경

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.0.6', '192.168.0.17', '127.0.0.1']

DJANGO_APPS += []
PROJECT_APPS += []
THIRD_PARTY_APPS += [
    'debug_toolbar',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [BASE_DIR / 'static']