"""
Django settings for jeweller project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print('Base dir is ', BASE_DIR)


# gain access to env.py file:
if os.path.exists('env.py'):
    print('env.py exists within os.path')
    import env
else:
    print('env.py does not exist within os.path')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in os.environ

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
                          'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
                            'allauth.account.auth_backends.AuthenticationBackend',
                            ]

SITE_ID = 1

# ACCOUNT_FORMS: Used to override the builtin forms.
# (Otherwise forms are found in templates/allauth/account Defaults to:
# DMcC 17/02/24 am removing the custom signup form as think its actually causing some confusion.abs
# This has already been handled in BA walkthrough - registration creates user with signal to create UserProfile with default settings
# The signed-in person can then modify their UserProfile
# Actually - reinstating as I want to capture firstname and lastname if possible on the UP
#
ACCOUNT_FORMS = {
                'signup': 'jeweller.forms.CustomSignupForm',
                }

ACCOUNT_VERIFICATION_METHOD = "username_email"
# Login method to use -userame/email/either (AllAuth 0.60.0)
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
# The user must link an email address when signing up.
ACCOUNT_EMAIL_REQUIRED = True
# Email verification at signup – mandatory/ optional/none
ACCOUNT_EMAIL_VERIFICATION = "none"
# When signing up, require emailx2?
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False
# When signing up, force the user to type in their password x2?
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

# An integer specifying the minimum allowed length of a username.
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
# Controls the life time of the session.
# Set to None to ask the user (“Remember me?”),
# False to not remember, and True to always remember.
ACCOUNT_SESSION_REMEMBER = None

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


ALLOWED_HOSTS = ['8000-deemccart-cipp5jeweller-10k3i9z0k0t.ws-eu107.gitpod.io',
                'https://8000-deemccart-cipp5jeweller-10k3i9z0k0t.ws-eu107.gitpod.io/',
                '8000-deemccart-cipp5jeweller-10k3i9z0k0t.ws-eu108.gitpod.io',
                 '.jeweller-bd1caeb15bbd.herokuapp.com',
                 'https://jeweller-bd1caeb15bbd.herokuapp.com/',
                 ]

CSRF_TRUSTED_ORIGINS = [
                       'https://8000-deemccart-cipp5jeweller-10k3i9z0k0t.ws-eu107.gitpod.io',
                       'https://8000-deemccart-cipp5jeweller-10k3i9z0k0t.ws-eu108.gitpod.io',
                       'https://jeweller-bd1caeb15bbd.herokuapp.com/'
                       ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'django.contrib.sites',
    'django_summernote',
    'cloudinary',
    'cloudinary_storage',
    'whitenoise',
    'gunicorn',

    # Apps
    'home',
    'profiles',
    'products',
    'basket',
    'checkout',

    # Other
    'crispy_forms',
    'crispy_bootstrap5',
    'storages',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
    # DMcC 06/02/24 Add debug toolbar middleware
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'jeweller.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'templates', 'allauth')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'basket.contexts.basket_contents',
            ],
        'builtins': [
                    'crispy_forms.templatetags.crispy_forms_tags',
                    'crispy_forms.templatetags.crispy_forms_field',
                    ],
        },
    },
]

WSGI_APPLICATION = 'jeweller.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
print('Database setting is ', DATABASES)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (f'django.contrib.auth.password_validation.'
        + 'UserAttributeSimilarityValidator'),
    },
    {
        'NAME': (f'django.contrib.auth.password_validation.MinimumLengthValidator'),
    },
    {
        'NAME': (f'django.contrib.auth.password_validation.'
                 +'CommonPasswordValidator'),
    },
    {
        'NAME': (f'django.contrib.auth.password_validation.'
                + 'NumericPasswordValidator'),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
print('Media root is ', MEDIA_ROOT)

if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
        }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'ci-pp5-jeweller'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# Media Files (Images) - Cloudinary
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

FREE_DELIVERY_THRESHOLD = 100
SITE_CURRENCY = "EUR"
SITE_CURRENCY_SYMBOL = "€"
STANDARD_DELIVERY_PERCENTAGE = 10
STANDARD_DELIVERY_AMOUNT = 7
FIRST_ORDER_NUMBER = 24004
FIRST_LINE_NUMBER = 10

STRIPE_CURRENCY = 'EUR'

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')

if 'DEV_EMAIL' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'Jewellery@example.com'
    DEFAULT_CC_EMAIL = os.environ.get('DEFAULT_CC_EMAIL')
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
    DEFAULT_CC_EMAIL = os.environ.get('DEFAULT_CC_EMAIL')
