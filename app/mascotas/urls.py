from django.urls import path

from . import views

app_name = "mascotas"
urlpatterns = [
    path("", views.index, name="index"),
]
