import os

from .base import *
from .utils import retornar_urls

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"
LOCAL_IPS = ["localhost", "127.0.0.1"]

ALLOWED_HOSTS = [retornar_urls()[-1]] + LOCAL_IPS
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Python Debug Toolbar
if DEBUG:
    import socket

    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    # Obtener IP de Docker
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + LOCAL_IPS
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": "debug_toolbar.middleware.show_toolbar_with_docker",
    }
