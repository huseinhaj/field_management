"""
Django settings for field_management project.
"""
import os
GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')
AUTH_USER_MODEL = 'field_app.CustomUser'
#pip install django-debug-toolbar
AUTHENTICATION_BACKENDS = [
    'field_app.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]
from pathlib import Path
import os  # Add this line at the very top
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# ============================================
# EMAIL CONFIGURATION - REAL GMAIL
# ============================================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # ✅ TUNA HII TU!
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'huseinhaj09@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'lexmdrrljvyxqplo')

DEFAULT_FROM_EMAIL = 'Field Management System <huseinhaj09@gmail.com>'
SERVER_EMAIL = 'huseinhaj09@gmail.com'
EMAIL_TIMEOUT = 30

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fb+ynjt%l-8!48f7(t*_xekmcj%lkbo9m%p$qs5pn=moj@@41i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = [
    '.onrender.com',
    'localhost',
    '127.0.0.1'
]
# ... (rest of your settings remain the same) ...


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',  
    'field_app', 
    'import_export',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
ROOT_URLCONF = 'field_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # project-level templates
            os.path.join(BASE_DIR, 'field_app/templates/field_app'),  # app-specific templates
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'field_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

import dj_database_url

# Use DATABASE_URL from Render environment
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    # Fallback for local development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'field_db'),
            'USER': os.environ.get('DB_USER', 'hajiuser'),
            'PASSWORD': os.environ.get('DB_PASSWORD', 'hajipassword'),
            'HOST': os.environ.get('DB_HOST', 'localhost'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        }
    }



# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = 'login'  # Name of your login URL pattern
LOGIN_REDIRECT_URL = 'dashboard'  # Where to redirect after login
LOGOUT_REDIRECT_URL = 'login'  # Where to redirect after logou

