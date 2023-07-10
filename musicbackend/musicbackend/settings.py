from pathlib import Path
import os
# import environ
from celery.schedules import crontab

import instruments.tasks

BASE_DIR = Path(__file__).resolve().parent.parent

# env = environ.Env()
# environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))

SECRET_KEY = "django-insecure-m!b^@r&jm*49nf2u!2t@sfmv!j$xuij6^c5wnv0j9$22y86!!e"
# SECRET_KEY = env('SECRET_KEY')

DEBUG = True
# DEBUG = env('DEBUG')

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 'django.contrib.sites',
    "instruments.apps.InstrumentsConfig",
    "rest_framework",
    "corsheaders",
    "django_filters",
    'drf_yasg',
    'django_celery_beat',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'instruments.middleware.SaveRequest'
]

ROOT_URLCONF = "musicbackend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = "musicbackend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = []

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}


CORS_ORIGIN_ALLOW_ALL = True

# CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_BEAT_SCHEDULE = {
    "sample_task": {
        "task": "instruments.tasks.send_report",
        "schedule": crontab(minute="*/15"),
    },
    "get_cache": {
        'task': 'instruments.tasks.get_cache',
        "schedule": crontab(minute="*/1"),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mailhog'
EMAIL_PORT = '1025'

SITE_ID = 2
ACCOUNT_EMAIL_VERIFICATION = 'none'

# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400
# ACCOUNT_LOGOUT_REDIRECT_URL ='/accounts/login/'
LOGIN_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        # "KEY_PREFIX": "example"
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# CENTRIFUGO_PORT = 8802
# the centrifugo message channel, do not change this value
# CENTRIFUGO_MESSAGE_NAMESPACE = "messages"
# the centrifugo thread channel, do not change this value
# CENTRIFUGO_THREAD_NAMESPACE = "threads"
# centrifugo config
# note that the following settings refer to centrifugE_...
# because it is the old name of the project
# change this to your domain/your port in production
# CENTRIFUGE_ADDRESS = 'http://localhost:{0}/'.format(CENTRIFUGO_PORT)
# change this to the key you put in config.json (see above)
# CENTRIFUGE_SECRET = 'django-insecure-m!b^@r&jm*49nf2u!2t@sfmv!j$xuij6^c5wnv0j9$22y86!!e'
# CENTRIFUGO_API_KEY = ''
# CENTRIFUGE_TIMEOUT = 5
