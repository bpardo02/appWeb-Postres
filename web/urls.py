from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="indice"),
    path("acerca", views.about, name="acerca"),
    path("bienvenido", views.welcome, name="bienvenido"),
    path("contacto", views.contact, name="contacto"),
    path("exito", views.exito, name="exito"),
    path("detalle/<uuid:flan_uuid>/", views.flan_detail, name="flan_detail"),
    path(
        "toggle_favorite_flan/<uuid:flan_uuid>/",
        views.toggle_favorite_flan,
        name="toggle_favorite_flan",
    ),
    path("favoritos/", views.favorite_flans, name="favorite_flans"),
]
