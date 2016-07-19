# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'hostname',
        'PORT': '3306',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1234567890'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
