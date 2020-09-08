from django.contrib import admin
from django.urls import path, include
from bodegas import views
urlpatterns = [
    path('tabla/', views.Tabla, name="Tabla"),
    path('agregarmaterial/', views.agregarma, name="agregarma"),
    path('modificarmaterial/<int:pk>', views.editarma, name="modificarmaterial"),
    path('eliminarmaterial/<int:pk>', views.borrarma, name="eliminarma"),
]
