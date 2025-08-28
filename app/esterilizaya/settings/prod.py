from .base import *
from .utils import retornar_urls

DEBUG = False
ADMINS = [("José Jácome", "josejacomeb@gmail.com")]
ALLOWED_HOSTS = [*retornar_urls(), "localhost"]
STATIC_ROOT = BASE_DIR / "static"

# Configuraciones de seguridad
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
