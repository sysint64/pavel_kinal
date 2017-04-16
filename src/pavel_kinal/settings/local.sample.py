from pavel_kinal.settings.base import *

DEBUG = True
SECRET_KEY = 'demo'

ALLOWED_HOSTS = [
    "*"
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOCALE_PATHS = (
    os.path.join(VAR_ROOT, 'locale'),
)
