import os
import base #NOQA

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static')
]

