from .base import *

ALLOWED_HOSTS = ['54.180.194.240']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbpybo',
        'USER': 'dbpybouser',
        'PASSWORD': 'dbpybouser',
        'HOST': 'ls-335257acf3f39d849f7eb034cc88bdb0d527a9a3.c36vvyyhk7pk.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}