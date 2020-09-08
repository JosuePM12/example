from django.contrib import admin
from django.urls import path, include
from Mecanico import views

urlpatterns = [
    path('lista/', views.lista, name="lista"),
    path('agregarmecanico/', views.agregarmecanico, name="agregarmecanico"),
    path('modificarmecanico/<int:pk>', views.modificarmecanico, name="modificarmecanico"),

]
