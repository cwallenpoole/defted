from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v06)+(3t!%rdg7z64rragy8c(#k(t5-x!y&9_qlk&d9qzvh)h='


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
