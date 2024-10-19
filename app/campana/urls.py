from django.urls import path

from . import views

app_name = "campana"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:year>/<str:parroquia>/<str:barrio>/", views.mostrar, name="mostrar"),
]
