from django.http import request
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

# Create your views here.
from .forms import bodegaForm, Bodega
def Tabla(request, plantilla="bodegas.html"):
    bodegas = Bodega.objects.all()
    data = {
        'bodega':bodegas
    }
    return render(request, plantilla, data)

##   pagina de crear o insertar INSERT
def agregarma(request, plantilla="agregar.html"):

    if request.method == "POST":
        form = bodegaForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('bodega')
    else:
        form = bodegaForm

    return render(request, plantilla, {'form': form})

## pagina de modificar o update
def editarma(request, pk, plantilla="modificar.html"):

    if request.method == "POST":
        bodega = get_object_or_404(Bodega, pk=pk)
        form = bodegaForm(request.POST or None, instance=bodega)
        if form.is_valid():
            form.save()
            return redirect('bodega')
    else:
        bodega = get_object_or_404(Bodega, pk=pk)
        form = bodegaForm(request.POST or None, instance=bodega)

    return render(request, plantilla, {'form': form})

## pagina de eliminar o delete
def borrarma(request, pk, plantilla="eliminar.html"):

    if request.method == "POST":
        form = bodegaForm((request.POST or None))
        bodega = get_object_or_404(Bodega, pk=pk)
        if form.is_valid():
            bodega.delete()
            return redirect('bodega')
    else:
        bodega = get_object_or_404(Bodega, pk=pk)
        form = bodegaForm(request.POST or None, instance=bodega)

    return render(request, plantilla, {'form': form})

