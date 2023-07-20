from logging import getLogger
from os import getenv
from sys import argv
from pathlib import Path


DEBUG = getenv('DEBUG', default=True)
SECRET_KEY = getenv('SECRET_KEY')
if not SECRET_KEY and DEBUG:
    SECRET_KEY = 'django-insecure-#g)gm9#!v9c0@w4_y-r$-#me&8oi^1d%5nc#tb8gi0p%64+=@m'

ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', default=['app'])

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'api.authapp.apps.AuthappConfig',
    'api.storageapp.apps.StorageappConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'k9174a.urls'

WSGI_APPLICATION = 'k9174a.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': getenv('POSTGRES_DB'),
        'USER': getenv('POSTGRES_USER'),
        'PASSWORD': getenv('POSTGRES_PASSWORD'),
        'HOST': getenv('POSTGRES_HOST'),
        'PORT': getenv('POSTGRES_PORT')
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'k9174a': {
            'format': '[%(levelname).1s %(asctime)s] %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'k9174a'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = BASE_DIR / 'storage'

logger = getLogger('django')

# Settings for development
if DEBUG:
    MIDDLEWARE.append('corsheaders.middleware.CorsMiddleware')
    CORS_ALLOWED_HEADERS = ['127.0.0.1:3000', 'localhost:3000']
    logger.warning(f'Using CORS headers: {CORS_ALLOWED_HEADERS}')
    logger.warning(f'Using database connection: {DATABASES["default"]}')

# Settings for unit-tests
if 'test' in argv:
    DEFAULT_FILE_STORAGE = 'api.storageapp.storages.InMemoryStorage'
    logger.warning(f'Using {DEFAULT_FILE_STORAGE} for tests')
