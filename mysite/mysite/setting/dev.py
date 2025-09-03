from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a+9lc+v)u-4f%=c6jotdlj3*6vnukfk34dk=13e7a(o9p$@9ca'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#CSRF_COOKIE_SECURE=True

SUMMERNOTE_THEME = 'bs4'

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_ROOT=BASE_DIR / 'static'
MEDIA_ROOT=BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS = "SAMEORIGIN"