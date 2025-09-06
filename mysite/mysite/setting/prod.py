from mysite.settings import *
DEBUG = True
CSRF_COOKIE_SECURE=True

SUMMERNOTE_THEME = 'bs4'

#ALLOWED_HOSTS = ['hosseinghorbanzadeh.com ','www.hosseinghorbanzadeh.com']
ALLOWED_HOSTS=[]

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