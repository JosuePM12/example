from django.shortcuts import render

# Create your views here.


def home(request, plantilla="home.html"):
    return render(request, plantilla)

def about(request, plantilla="about.html"):
    return render(request, plantilla)

def contact(request, plantilla="contact.html"):
    return render(request, plantilla)

def bodega(request, plantilla="bodega.html"):
    return render(request, plantilla)

def usuario(request, plantilla="usuario.html"):
    return render(request, plantilla)

def factura(request, plantilla="factura.html"):
    return render(request, plantilla)

def mecanico(request, plantilla="Mecanico.html"):
    return render(request, plantilla)

def citarapida(request, plantilla="citarapida.html"):
    return render(request, plantilla)