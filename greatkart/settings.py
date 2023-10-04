from pathlib import Path
from django.contrib.messages import constants as messages
import pymysql
pymysql.install_as_MySQLdb()

import environ
import os
# import django_heroku
import dj_database_url

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = '02-hpz3zu3=+_bir40yb-(lx3qfj$c0eq+t)$ahv2h*mq!382g'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'category',
    'store',
    'carts',
    'accounts',
    'orders',
    'admin_honeypot',
    'shop',

]

INSTALLED_APPS += ('django_summernote', )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'greatkart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter',
            ],
        },
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

WSGI_APPLICATION = 'greatkart.wsgi.application'

AUTH_USER_MODEL = 'accounts.Account'    # Tên model thay thế cho model user mặc định


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eemqimae_data',
        'USER': 'eemqimae_user',
        'PASSWORD': 'Manager$2023',
        'HOST': '102.219.176.39',
        'PORT': '3306',

        #'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'ldb',
        #'USER': 'root',
        #'PASSWORD': '',
        #'HOST': '127.0.0.1',
        #'PORT': '3306',
        
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
#STATICFILES_DIRS = [
#   'greatkart/static'
#]
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static/'),
)

# django_heroku.settings(locals())


# Cầu hình media file
MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.WARNING: 'warning',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.DEBUG: 'secondary'
}



#EMAIL_HOST = env("EMAIL_HOST")
#EMAIL_HOST_USER = env("EMAIL_HOST_USER")
#EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
#EMAIL_PORT = env("EMAIL_PORT")
#EMAIL_HOST='smtp.gmail.com'
#EMAIL_HOST_USER='anhnguyenlam171@gmail.com'
#EMAIL_HOST_PASSWORD='lwdjiwrzkvpdxgtn'
#EMAIL_PORT=587


#EMAIL_USE_TLS = True
#EMAIL_HOST='smtp.gmail.com'
#EMAIL_HOST_USER='anhnguyenlam171@gmail.com'
#EMAIL_HOST_PASSWORD='lwdjiwrzkvpdxgtn'
#EMAIL_PORT=587

