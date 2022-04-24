from homebase.settings.base import *

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
#SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = '!sls2(u-2^+*(ob%hc5xrifx0i#ekgguj%c3i_k@ia001w$it0'

DEBUG = False
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '/shared/homebase.sqlite3'),
    }
}
