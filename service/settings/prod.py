import os
from .url_regex import *
from .common import *
from .gimmeproxy import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "api.enginyuksel.kim"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'md',
        'USER': 'md',
        'PASSWORD': 'md159qq!',
        'HOST': 'localhost',
        'PORT': '',
    }
}


STATIC_URL = '/static/'
