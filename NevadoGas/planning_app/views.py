from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, "sites/inicio.html")

def nosotros(request):
    return render(request, "sites/nosotros.html")

def municipio(request):
    return render(request, "inventario/index.html")