from .base import *
from .utils import retornar_urls

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [retornar_urls()[-1], "localhost"]
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
