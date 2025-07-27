from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*", "localhost"]
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
