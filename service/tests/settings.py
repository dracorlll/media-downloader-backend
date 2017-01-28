from __future__ import absolute_import
from settings.common import *
import os


BASE_DIR = os.path.dirname(__file__)
# SECRET_KEY = SECRET_KEY

ROOT_URLCONF = 'tests.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test.db'),
    }
}

DEBUG = True

TEMPLATE_DEBUG = True

INSTALLED_APPS += (
    'tests',
)

TESTING = True

