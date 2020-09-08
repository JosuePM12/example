from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

# Create your views here.
from .forms import MecanicoForm, Mecanico
def lista(request, plantilla="Mecanico.html"):
    mecanicos = Mecanico.objects.all()
    data = {
        'Mecanico':mecanicos
    }
    return render(request, plantilla, data)

##   pagina de crear o insertar INSERT
def agregarmecanico(request, plantilla="agregarmecanico.html"):

    if request.method == "POST":
        form = MecanicoForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('Mecanico')
    else:
        form = MecanicoForm

    return render(request, plantilla, {'form': form})
#modificar
def modificarmecanico(request, pk, plantilla="modificarmecanico.html"):

    if request.method == "POST":
        mecanico = get_object_or_404(Mecanico, pk=pk)
        form = MecanicoForm(request.POST or None, instance=mecanico)
        if form.is_valid():
            form.save()
            return redirect('mecanico')
    else:
        mecanico = get_object_or_404(Mecanico, pk=pk)
        form = MecanicoForm(request.POST or None, instance=mecanico)

    return render(request, plantilla, {'form': form})