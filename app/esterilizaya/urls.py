"""
URL configuration for esterilizaya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("inicio.urls", namespace="inicio")),
    path("admin/", admin.site.urls),
    path("inscripcion/", include("inscripcion.urls", namespace="inscripcion")),
    path("campana/", include("campana.urls", namespace="campana")),
    path("registro/", include("registro.urls", namespace="registro")),
    path("cuenta/", include("cuenta.urls", namespace="cuenta")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
