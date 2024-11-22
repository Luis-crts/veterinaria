from django.http import HttpResponse
from django.shortcuts import render
from .modelos import Publicacion
from django.shortcuts import get_object_or_404
from datetime import date
from django.db.models import Q


def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'lista_publicaciones.html', {'publicaciones': publicaciones})

def index(request):
    return HttpResponse("¡Bienvenido al sitio de Veterinaria!")

from django.db.models import Q

def lista_gatos(request):
    query = request.GET.get('nombre', '')
    categoria = request.GET.get('categoria', '')

    # Construir el filtro
    filtros = Q()
    if query:
        filtros &= Q(nombre__icontains=query)
    if categoria:
        filtros &= Q(categoria=categoria)
    else:
        filtros &= Q(categoria__in=['gato', 'perro'])  # Mostrar ambas categorías si no hay filtro

    gatos = Publicacion.objects.filter(filtros)

    return render(request, 'lista_gatos.html', {'gatos': gatos, 'query': query, 'categoria': categoria})


def detalle_gato(request, gato_id):
    gato = get_object_or_404(Publicacion, id=gato_id)
    dias_para_pipeta = gato.dias_para_proxima_pipeta() 
    dias_para_vacuna = gato.dias_para_proxima_vacuna()
    return render(request, 'detalle_gato.html', {
        'gato': gato,
        'dias_para_pipeta': dias_para_pipeta,
        'dias_para_vacuna': dias_para_vacuna
    })