from base import *
from .passwords import DB_PWD


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_template_fiddle',
        'USER': 'postgres',
        'PASSWORD': DB_PWD,
        'HOST': '',
        'PORT': '5433'
    }
}

GOOGLE_ANALYTICS_FLAG = 0
