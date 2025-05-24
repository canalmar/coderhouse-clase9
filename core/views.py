from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        "nombre": "vero",
        "rol": "tutora"
    }
    return render(request,"core/index.html", context)

def saludar(request):
    return HttpResponse("Hola desde Django!")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1 style='color:red'>HOLA</h1>")

def saludar_con_parametros(request,nombre:str, apellido:str):
    nombre = nombre.capitalize()
    apellido = apellido.upper()
    return HttpResponse(f"{apellido}, {nombre}")

