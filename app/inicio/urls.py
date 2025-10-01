from django.urls import path

from . import views

app_name = "inicio"

urlpatterns = [
    path("campanas", views.index, name="index"),
    path("", views.home, name="home"),
]
