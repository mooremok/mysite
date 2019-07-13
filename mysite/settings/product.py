import os
from .base import *


SECRET_KEY = '=99ny#f@9p)o(ntrv!89+8)*hs7!ig0of#t$j&gng^8^x#6k6@'

DEBUG = False

ALLOWED_HOSTS = ['47.111.181.112', 'www.tabworld.cn', 'tabworld.cn']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite_db',
        'USER': 'root',
        'PASSWORD': 'guoyiling0320',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, 'static')
#]

ADMINS = (
    ('admin', 'mooremok@163.com'),
)

# 日志文件
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/mysite_debug.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

