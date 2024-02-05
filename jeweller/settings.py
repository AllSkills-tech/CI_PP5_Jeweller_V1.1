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
# import dj_database_url DMcC 31/01/24:  Added to align with walkthrough, but not yet installed for project

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(f'Base dir is ',BASE_DIR)


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
    'allauth.account.auth_backends.AuthenticationBackend',]

SITE_ID=1

ACCOUNT_FORMS = {
'signup': 'jeweller.forms.CustomSignupForm',
}
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_VERIFICATION_METHOD='username_email'
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_VERIFICATION='None'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE=False
ACCOUNT_USERNAME_MIN_LENGTH=4
LOGIN_URL='/accounts/login/'
LOGIN_REDIRECT_URL='/'

MESSAGE_STORAGE='django.contrib.messages.storage.session.SessionStorage'


ALLOWED_HOSTS = ['8000-deemccart-cipp5jeweller-10k3i9z0k0t.ws-eu107.gitpod.io', 
                'https://8000-deemccart-cipp5jeweller-10k3i9z0k0t.ws-eu107.gitpod.io/',
                '8000-deemccart-cipp5jeweller-10k3i9z0k0t.ws-eu108.gitpod.io',    

                 '.jeweller-bd1caeb15bbd.herokuapp.com',
                 'https://jeweller-bd1caeb15bbd.herokuapp.com/',
                ]

CSRF_TRUSTED_ORIGINS = ['https://8000-deemccart-cipp5jeweller-10k3i9z0k0t.ws-eu107.gitpod.io', 
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
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.sites',
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
    'allauth.account.middleware.AccountMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
print(f'Staticfiles dirs is ', STATICFILES_DIRS)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticCloudinaryStorage'
# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
#CLOUDINARY_STORAGE = {
#    'CLOUD_NAME': os.environ['CLOUDINARY_CLOUD_NAME'],
#    'API_KEY': os.environ['CLOUDINARY_API_KEY'],
#    'API_SECRET': os.environ['CLOUDINARY_API_SECRET'],
#}
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
print(f'Media root is ', MEDIA_ROOT)

if 'USE_AWS' in os.environ:
   # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    # Bucket Config
#    AWS_STORAGE_BUCKET_NAME = 'reloved-6745667db3c5'
#    AWS_S3_REGION_NAME = 'eu-west-1'
#    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
#    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
#    STATICFILES_LOCATION = 'static'
#    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
#    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
#    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
#    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'



# Media Files (Images) - Cloudinary
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

MESSAGE_STORAGE='django.contrib.messages.storage.session.SessionStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BUSINESS_NAME = 'FreddyTheDawg'
FREE_DELIVERY_THRESHOLD = 75
SITE_CURRENCY = "EUR"
SITE_CURRENCY_SYMBOL ="€"
STANDARD_DELIVERY_PERCENTAGE = 10
STANDARD_DELIVERY_AMOUNT = 7
FIRST_ORDER_NUMBER = 24004
FIRST_LINE_NUMBER = 10

STRIPE_CURRENCY = 'EUR'

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')


print(STRIPE_CURRENCY)
