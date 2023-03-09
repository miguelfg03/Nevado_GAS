from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path("nosotros", views.nosotros, name ='nosotros'),
    path("inventario", views.municipio, name ="inventario"),
    path('inventario/crear', views.create_municipio, name = "create"),
    path('inventario/editar', views.edit_municipio, name = "edit"),
]
