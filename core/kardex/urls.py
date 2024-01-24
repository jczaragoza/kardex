from unicodedata import name
from django.urls import path
from core.kardex.views.curso.views import *
from core.kardex.views.persona.views import *
from core.kardex.views.vehiculo.views import *
from core.kardex.views.kardex.views import *
from core.kardex.views.arma.views import *
from core.kardex.views.puesto.views import *
from core.kardex.views.consulta.views import *
from core.kardex.views.dashboard.views import *
from core.kardex.views.bienes.views import *
from core.kardex.views.reportes.views import *

from django.conf.urls import include

app_name = 'kardex'

urlpatterns = [
    #PERSONA
    path('persona/', PersonaListView.as_view(), name='persona_list'),
    path('persona/add/', PersonaCreateView.as_view(), name='persona_create'),
    path('persona/update/<int:pk>/', PersonaUpdateView.as_view(), name='persona_update'),
    path('persona/delete/<int:pk>/', PersonaDeleteView.as_view(), name='persona_delete'),
    path('persona/detail/<int:pk>/', PersonaDetailView.as_view(), name='persona_detail'),

    #CURSOS
    path('curso/', CursoListView.as_view(), name='curso_list'),
    path('curso/add/', CursoCreateView.as_view(), name='curso_create'),
    path('curso/update/<int:pk>/', CursoUpdateView.as_view(), name='curso_update'),
    path('curso/delete/<int:pk>/', CursosDeleteView.as_view(), name='curso_delete'),

    #VEHÍCULOS
    path('vehiculo/', VehiculoListView.as_view(), name='vehiculo_list'),
    path('vehiculo/add/', VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('vehiculo/update/<int:pk>/', VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path('vehiculo/delete/<int:pk>/', VehiculoDeleteView.as_view(), name='vehiculo_delete'),

    #ARMAS
    path('arma/', ArmaListView.as_view(), name='arma_list'),
    path('arma/add/', ArmaCreateView.as_view(), name='arma_create'),
    path('arma/update/<int:pk>/', ArmaUpdateView.as_view(), name='arma_update'),
    path('arma/delete/<int:pk>/', ArmaDeleteView.as_view(), name='arma_delete'),

    #PUESTOS
    path('puesto/', PuestoListView.as_view(), name='puesto_list'),
    path('puesto/add/', PuestoCreateView.as_view(), name='puesto_create'),
    path('puesto/update/<int:pk>/', PuestoUpdateView.as_view(), name='puesto_update'),
        
    #DASHBOARD
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
   
    #KARDEX
    path('kardex/add/', KardexCreateView.as_view(), name='kardex_create'),
    path('kardex/list/', KardexListView.as_view(), name='kardex_list'),
    #path('kardex/update/<int:pk>/', kardexUpdateView.as_view(), name='kardex_update'),
    path('kardex/delete/<int:pk>/', kardexDeleteView.as_view(), name='kardex_delete'),

    #CONSULTA
    path('consulta/', PersonaConsultaView.as_view(), name='persona_consulta'),
    path('consulta/add/', PersonaAddView.as_view(), name='persona_add'),
    path('consulta/detail/<int:pk>/', ConsultaDetailView.as_view(), name='consulta_detail'),
    path('consulta/update/<int:pk>/', ConsultaUpdateView.as_view(), name='consulta_detail'),

    #BIENES
    path('bienes/', BienesListView.as_view(), name='bienes_list'),
    path('bienes/add/', BienesCreateView.as_view(), name='bienes_create'),
    path('bienes/update/<int:pk>/', BienesUpdateView.as_view(), name='bienes_update'),
    path('bienes/delete/<int:pk>/', BienesDeleteView.as_view(), name='bienes_delete'),

    #REPORTES
    path('reportes/', ReportesListView.as_view(), name='reportes_list'),
    
]
