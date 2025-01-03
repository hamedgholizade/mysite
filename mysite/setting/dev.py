from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p&uq7=g$xuvo5*4d0pc-z+3l=&kava#4l63gne&j1)a8q(yq3i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#INSTALLED_APPS = []

#SITE_FRAMEWORK
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_ROOT = 'media'
STATIC_ROOT = 'static'

STATICFILES_DIRS = [
    BASE_DIR / "statics",]

X_FRAME_OPTIONS = "SAMEORIGIN"