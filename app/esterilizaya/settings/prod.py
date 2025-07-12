from .base import *

DEBUG = False
ADMINS = [("José Jacome", "josejacomeb@gmail.com")]
ALLOWED_HOSTS = ["happypawspillaro.org", "www.happypawspillaro.org"]
STATIC_ROOT = BASE_DIR / "static"

# Configuraciones de seguridad
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
