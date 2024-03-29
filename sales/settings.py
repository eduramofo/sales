from pathlib import Path
from decouple import config, Csv
from dj_database_url import parse as dburl
from . import apps

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='NOT_GOOD_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

INTERNAL_IPS = ('127.0.0.1',)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

ADMINS = [
    ('Eduardo Rabelo', 'eduramofo@gmail.com'),
]

SERVER_EMAIL = "Edu Fontes <eduramofo@gmail.com>"

# Application definition

INSTALLED_APPS = apps.APPS

SITE_ID = 1

MIDDLEWARE = [

    # django
    'django.middleware.security.SecurityMiddleware',

    # thirds/whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # django
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'sales.urls'

CUSTOM_TEMPLATES =  BASE_DIR / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [CUSTOM_TEMPLATES],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.globallabel',
                'account.context_processors.current_account',
            ],
        },
    },
]

WSGI_APPLICATION = 'sales.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

default_dburl = 'postgres://postgres:postgres@localhost:5432/sales'
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#########################################################
# AWS - START
#########################################################
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
AWS_STORAGE_BUCKET_NAME = config('AWS_S3_STORAGE_BUCKET_NAME', default='')
AWS_S3_SIGNATURE_VERSION = config('AWS_S3_SIGNATURE_VERSION', default='')
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_IS_GZIPPED = True
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
AWS_STATIC_LOCATION = 'static'
AWS_STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
AWS_PUBLIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_PUBLIC_MEDIA_LOCATION)
#########################################################
# AWS - END
#########################################################


#########################################################
# MEDIA - START
#########################################################

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE', default='django.core.files.storage.FileSystemStorage')

PRIVATE_FILE_STORAGE = config('PRIVATE_FILE_STORAGE', default='django.core.files.storage.FileSystemStorage')

#########################################################
# MEDIA - END
#########################################################


#########################################################
# STATIC - START
#########################################################
# STATIC
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = config('STATICFILES_STORAGE', default='whitenoise.storage.CompressedManifestStaticFilesStorage')

STATIC_URL = config('STATIC_URL', default='/static/')
#########################################################
# STATIC - END
#########################################################


#########################################################
# Security configuration - START
#########################################################
SECURE_PROXY_SSL_HEADER = config('SECURE_PROXY_SSL_HEADER', default=(''), cast=Csv())

SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)

SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)

CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool)
#########################################################
# Security configuration - END
#########################################################


#########################################################
# Email configuration - START
#########################################################
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='127.0.0.1')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='webmaster@localhost')
#########################################################
# Email configuration - END
#########################################################


#########################################################
# Celery Configuration Options
#########################################################
# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html#using-celery-with-django
# https://youtu.be/BbPswIqn2VI?t=301
# https://docs.celeryproject.org/en/stable/userguide/configuration.html
CELERY_BROKER_URL = config('CELERY_BROKER_URL', default='redis://127.0.0.1:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TIMEZONE = 'America/Sao_Paulo'
CELERY_TASK_TRACK_STARTED = True
BROKER_POOL_LIMIT = None
#########################################################
# Celery Configuration Options
#########################################################


#########################################################
# Telegram BOT - START
#########################################################
TELEGRAM_BOT_API = config('TELEGRAM_BOT_API', default='')
TELEGRAM_BOT_CHAT_ID = config('TELEGRAM_BOT_CHAT_ID', default='')
#########################################################
# Telegram BOT - END
#########################################################

#########################################################
# Auth - START
#########################################################
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
#########################################################
# Auth - END
#########################################################


#########################################################
# CRISPY_TEMPLATE_PACK - START
#########################################################
CRISPY_TEMPLATE_PACK = 'bootstrap4'
#########################################################
# CRISPY_TEMPLATE_PACK - END
#########################################################
