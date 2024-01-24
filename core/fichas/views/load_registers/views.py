from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import View


#IMPORT MODEL AND FORM
from core.fichas.forms import *
from core.fichas.models import *

def cargar_registros_integrantes(request):
    registros = Integrantes.objects.all().values('id', 'nombre', 'cargo') 
    registros_list = list(registros)
    return JsonResponse(registros_list, safe=False)

def cargar_registros_cargos(request):
    registros = CargosPopulares.objects.all().values('id', 'nombre', 'detalles', 'periodo')
    registros_list = list(registros)
    return JsonResponse(registros_list, safe=False)

def cargar_registros_experiencia(request):
    registros = ExperienciaLaboral.objects.all().values('id', 'nombre', 'dependencia', 'periodo')
    registros_list = list(registros)
    return JsonResponse(registros_list, safe=False)

def cargar_registros_temas(request):
    registros = TemasAtencion.objects.all().values('id', 'nombre')
    registros_list = list(registros)
    return JsonResponse(registros_list, safe=False)

def cargar_registros_vehiculos(request):
    registros = Vehiculos.objects.all().values('id', 'marca', 'submarca', 'modelo', 'color', 'matricula')
    registros_list = list(registros)
    return JsonResponse(registros_list, safe=False)

def cargar_registros_domicilios(request):
    registros = Domicilios.objects.all().values('id', 'abrev', 'calle', 'numero_ext', 'numero_int', 'dpto', 'edificio', 'mzn', 'lote', 'colonia', 'municipio', 'estado', 'cp')
    registros_list = list(registros)
    return JsonResponse(registros_list, safe=False)

def cargar_registros_eventos(request):
    registros = Evento.objects.all().values('id', 'fecha_evento', 'nombre')
    registros_list = list(registros)
    return JsonResponse(registros_list, safe=False)


