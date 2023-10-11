from .base import *

# 운영환경

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # 운영하는 서버에서는 debug가 켜져있을 필요가 없음

ALLOWED_HOSTS = ['192.168.0.6', '192.168.0.17', '127.0.0.1', '43.200.176.59']

DJANGO_APPS += []
PROJECT_APPS += []
THIRD_PARTY_APPS += []

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_ROOT = BASE_DIR / 'static'