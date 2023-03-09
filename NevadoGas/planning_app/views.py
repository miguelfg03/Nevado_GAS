from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, "sites/inicio.html")

def nosotros(request):
    return render(request, "sites/nosotros.html")

def municipio(request):
    return render(request, "inventario/index.html")

def create_municipio(request):
    return render(request, "inventario/create.html")

def edit_municipio(request):
    return render(request, "inventario/edit.html")