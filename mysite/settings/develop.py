import os
from .base import * #NOQA

SECRET_KEY = '=99ny#f@9p)o(ntrv!89+8)*hs7!ig0of#t$j&gng^8^x#6k6@'

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static')
]

