# Django settings for anytask project.
# coding: utf-8

from anytask.settings_common import *
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost']

domain = os.environ.get('DOMAIN')
if domain is not None:
    ALLOWED_HOSTS.extend(domain.split(','))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.setdefault('POSTGRES_DB', 'postgres'),
        'USER': os.environ.setdefault('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.setdefault('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.setdefault('POSTGRES_HOST', ''),
        'PORT': os.environ.setdefault('POSTGRES_PORT', ''),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.setdefault('EMAIL_HOST', '')
EMAIL_PORT = os.environ.setdefault('EMAIL_PORT', '465')

EMAIL_HOST_USER = os.environ.setdefault('EMAIL_USER', '')
EMAIL_HOST_PASSWORD = os.environ.setdefault('EMAIL_PASSWORD', '')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
