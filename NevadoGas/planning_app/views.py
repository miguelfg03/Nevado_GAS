from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Municipio
from .forms import MunicipioForm
# Create your views here.

def inicio(request):
    return render(request, "sites/inicio.html")

def nosotros(request):
    return render(request, "sites/nosotros.html")

def municipio(request):
    municipios = Municipio.objects.all()
    return render(request, "inventario/index.html", {'municipios': municipios})

def create_municipio(request):
    formulario = MunicipioForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('inventario')
    return render(request, "inventario/create.html", {'formulario': formulario})

def edit_municipio(request, id):
    municipio = Municipio.objects.get(pk=id)
    formulario = MunicipioForm(request.POST or None, instance=municipio)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('inventario')
    return render(request, "inventario/edit.html", { 'formulario': formulario})

def delete_municipio(request, id):
    municipio = Municipio.objects.get(pk=id)
    municipio.delete()
    return redirect("inventario")