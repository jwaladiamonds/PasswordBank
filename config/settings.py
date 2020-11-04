from django.contrib import messages
from config.base import *


ALLOWED_HOSTS += ['*']


INSTALLED_APPS += [
    'crispy_forms',
    'accounts',
    'dashboard',
]

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES[0]['DIRS'] += [BASE_DIR / 'templates',]

STATIC_URL = '/assets/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = (BASE_DIR / 'assets',)

AUTH_USER_MODEL = 'accounts.User'

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/dashboard'
LOGOUT_REDIRECT_URL = '/'

LANGUAGE_CODE = 'en-in'

TIME_ZONE = 'Asia/Kolkata'
