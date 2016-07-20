# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db.sqlite3'),
    },
    'dealhunt': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'huy',
        'USER': 'huy',
        'PASSWORD': 'huy',
        'HOST': 'huy',
        'PORT': '3306',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'huy'

# SECURITY WARNING: don't run with debug turned on in production!

BROKER_URL = 'redis://localhost:6379'

REDIS_HOST = 'localhost'

REDIS_PORT = 6379
