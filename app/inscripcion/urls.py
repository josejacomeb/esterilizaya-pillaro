from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="inscripcion_index"),
]
