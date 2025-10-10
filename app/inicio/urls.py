from django.urls import path

from . import views

app_name = "inicio"

urlpatterns = [
    path("campanas", views.ver_campanas, name="ver_campanas"),
    path("", views.index, name="index"),
]
