"""
Django settings for pyconbalkan project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import raven
import sys
from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', config('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']
TAGGIT_CASE_INSENSITIVE = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'pyconbalkan.core',
    'pyconbalkan.conference',
    'pyconbalkan.speaker',
    'pyconbalkan.organizers',
    'pyconbalkan.about',
    'pyconbalkan.timetable',
    'pyconbalkan.sponsors',
    'pyconbalkan.cfp',
    'pyconbalkan.contact',
    'pyconbalkan.news',
    'pyconbalkan.coc',
    'pyconbalkan.info',
    'pyconbalkan.faq',
    # others
    'rest_framework',
    'django_countries',
    'markdownx',
    'raven.contrib.django.raven_compat',
    'meta',
    'taggit',
    'djmoney',
    'markdownify',
]

MIDDLEWARE = [
    # Django middlewares
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Custom middlewares
    'pyconbalkan.conference.middleware.ConferenceSelectionMiddleware',
]

ROOT_URLCONF = 'pyconbalkan.urls'
# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/cfps'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'loaders': [
                'pyconbalkan.core.loaders.PyconLoader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pyconbalkan.wsgi.application'
META_SITE_PROTOCOL = "https"
META_SITE_DOMAIN = "pyconbalkan.com"
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

PDF_ROOT = os.path.join(BASE_DIR, 'pyconbalkan/core/static/pdf/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'pyconbalkan/core/')
MEDIA_URL = '/'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

AWS_S3_SECRET_ACCESS_KEY = config("AWS_S3_SECRET_ACCESS_KEY", "")
AWS_S3_ACCESS_KEY_ID = config("AWS_S3_ACCESS_KEY_ID", "")
AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME", "")

LOGIN_URL = '/admin/'
META_DEFAULT_KEYWORDS = ['PyCon', 'Balkan']

if DEBUG:
    # Storage
    DEFAULT_FILE_STORAGE = "pyconbalkan.core.storage.LocalStorage"
    # Email
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = '/tmp/app-emails'
else:
    TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'
    SECURE_SSL_REDIRECT = False if TESTING else True
    # Storage
    DEFAULT_FILE_STORAGE = "pyconbalkan.core.storage.S3Storage"
    # Email
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = config("EMAIL_HOST", "")
    EMAIL_PORT = config("EMAIL_PORT", default="587", cast=int)
    EMAIL_HOST_USER = config("EMAIL_HOST_USER", "")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", "")
    EMAIL_USE_TLS = True
    # Sentry config
    RAVEN_CONFIG = {
        'dsn': config('SENTRY_DSN', ""),
        'string_max_length': 1000,
    }
    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                          '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                'tags': {'custom-tag': 'x'},
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        },
    }