import os
from typing import Tuple


def retornar_urls() -> Tuple[str, str, str]:
    """Retorna las URLs configuradas en las variables de entorno acorde a los ALLOWED_HOSTS
    de Django.

    Returns:
        Tuple[str, str, str]: APP_URL, APP_URL sin 'www.', LOCAL_URL
    """
    APP_URL = os.getenv("APP_URL", "www.happypawspillaro.org")  # APP URL del servidor, como en el .env
    LOCAL_URL = os.getenv("LOCAL_URL", "localhost")  # URL local para pruebas en red local
    return APP_URL, APP_URL.removeprefix("www."), LOCAL_URL
