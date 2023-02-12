"""
Django settings for jp2 project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from corsheaders.defaults import default_headers
import os
from decouple import config
import django_heroku
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# # Actual directory user files go to
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'mediafiles')

# # URL used to access the media
# MEDIA_URL = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = ["*"]

# ALLOWED_HOSTS = [
#     'localhost',
#     '127.0.0.1',
# ]

# Application definition

INSTALLED_APPS = [
    #'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'api.apps.ApiConfig',
    
    'rest_framework',
    'corsheaders',
    'debug_toolbar',
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware', #
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jp2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'jp2_react/build',
            os.path.join(BASE_DIR, 'jp2_react/build'),
            os.path.join(BASE_DIR, 'jp2_react/public')
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'jp2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'DATABASE_URL': config('DATABASE_URL'),
#         'PGDATABASE': config('PGDATABASE'),
#         'PGHOST': config('PGHOST'),
#         'PGPASSWORD': config('PGPASSWORD'),
#         'PGPORT': config('PGPORT'),
#         'PGUSER': config('PGUSER'),
#     }
# }

DATABASE_URL = config('DATABASE_URL')
DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#STATIC_URL = '/static/' ### zakomentovat
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
 #   BASE_DIR / 'static',
    BASE_DIR / 'jp2_react/build/static',
    # os.path.join(PROJECT_ROOT, 'static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',    #causes verbose duplicate notifications in django 1.9
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS_ALLOWED_ORIGINS = [
#     "https://example.com",
#     "https://sub.example.com",
#     "http://localhost:8080",
#     "http://127.0.0.1:9000",
# ]

CORS_ALLOW_ALL_ORIGINS = True  # v produkci nahradit předchozím 'CORS_ALLOWED_ORIGINS' a přidat příslušnou adresu

CORS_REPLACE_HTTPS_REFERER = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://172.18.94.53:3000",
]

CSRF_COOKIE_DOMAIN = ['.localhost', '127.0.0.1']

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

django_heroku.settings(locals())
