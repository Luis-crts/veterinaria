from django.http import HttpResponse
from django.shortcuts import render
from .modelos import Publicacion
from django.shortcuts import get_object_or_404
from datetime import date

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'lista_publicaciones.html', {'publicaciones': publicaciones})

def index(request):
    return HttpResponse("¡Bienvenido al sitio de Veterinaria!")

def lista_gatos(request):
    gatos = Publicacion.objects.filter(categoria='gato')  # Filtrar solo los gatos
    return render(request, 'lista_gatos.html', {'gatos': gatos})

def detalle_gato(request, gato_id):
    gato = get_object_or_404(Publicacion, id=gato_id)
    dias_para_pipeta = gato.dias_para_proxima_pipeta()  # Calcular días para pipeta
    dias_para_vacuna = gato.dias_para_proxima_vacuna()  # Calcular días para vacuna
    return render(request, 'detalle_gato.html', {
        'gato': gato,
        'dias_para_pipeta': dias_para_pipeta,
        'dias_para_vacuna': dias_para_vacuna
    })