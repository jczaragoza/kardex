from django.urls import path

from core.fichas.views.lideres.views import *
from core.fichas.views.organizaciones.views import *
from core.fichas.views.eventos.views import *
from core.fichas.views.captura_lider.views import *
from core.fichas.views.captura_org.views import *
from core.fichas.views.consulta_lider.views import *
from core.fichas.views.consulta_org.views import *
from core.fichas.views.load_registers.views import *
from core.fichas.views.partido.views import *

app_name = 'fichas'

urlpatterns = [

    #LÍDERES
    path('lider/list/', LiderListView.as_view(), name='lider_list'),
    path('lider/add/', LiderCreateView.as_view(), name='lider_create'),
    path('lider/update/<int:pk>/', LiderUpdateView.as_view(), name='lider_update'),
    path('lider/delete/<int:pk>/', LiderDeleteView.as_view(), name='lider_delete'),
    path('lider/detail/<int:pk>/', LiderDetailView.as_view(), name='lider_detail'),

    #ORGANIZACIONES
    path('org/list/', OrganizacionListView.as_view(), name='organizacion_list'),
    path('org/add/', OrganizacionCreateView.as_view(), name='organizacion_create'),
    path('org/update/<int:pk>/', OrganizacionUpdateView.as_view(), name='organizacion_update'),
    path('org/delete/<int:pk>/', OrganizacionDeleteView.as_view(), name='organizacion_delete'),
    path('org/detail/<int:pk>/', OrganizacionDetailView.as_view(), name='organizacion_detail'),

    #EVENTO
    path('evento/list/', EventoListView.as_view(), name='evento_list'), 
    path('evento/add/', EventoCreateView.as_view(), name='evento_create'),
    path('evento/update/<int:pk>/', EventoUpdateView.as_view(), name='evento_update'),
    path('evento/delete/<int:pk>/', EventoDeleteView.as_view(), name='evento_delete'),

    #CAPTURA_ORGANIZACIONES
    path('captura/org/list/', CapturaOrgListView.as_view(), name='captura_org_list'),
    path('captura/org/add/', CapturaOrgCreateView.as_view(), name='captura_org_add'),
    path('captura/org/update/<int:pk>/', CapturaOrgUpdateView.as_view(), name='captura_org_update'),
    path('captura/org/detail/<int:pk>/', CapturaOrgDetailView.as_view(), name='captura_org_detail'),

    #CAPTURA_LÍDERES
    path('captura/lider/list/', CapturaLiderListView.as_view(), name='captura_lider_list'),
    path('captura/lider/add/', CapturaLiderCreateView.as_view(), name='captura_lider_add'),
    path('captura/lider/update/<int:pk>/', CapturaLiderUpdateView.as_view(), name='captura_lider_update'),
    path('captura/lider/detail/<int:pk>/', CapturaLiderDetailView.as_view(), name='captura_lider_detail'),

    #CONSULTA
    path('consulta/org/list/', OrganizacionConsultaView.as_view(), name='consulta_org_list'),
    path('consulta/org/detail/<int:pk>/', OrganizacionConsultaDetailView.as_view(), name='consulta_org_detail'),
    path('consulta/lider/list/', ConsultaLiderListView.as_view(), name='consulta_lider_list'),
    path('consulta/lider/detail/<int:pk>/', ConsultaFichaDetalleView.as_view(), name='consulta_lider_detail'),

    #LOAD REGISTERS
    path('cargar_registros/integrantes/', cargar_registros_integrantes, name='cargar_registros_integrantes'),
    path('cargar_registros/cargos/', cargar_registros_cargos, name='cargar_registros_cargos'),
    path('cargar_registros/experiencia/', cargar_registros_experiencia, name='cargar_registros_experiencia'),
    path('cargar_registros/temas/', cargar_registros_temas, name='cargar_registros_temas'),
    path('cargar_registros/vehiculos/', cargar_registros_vehiculos, name='cargar_registros_vehiculos'),
    path('cargar_registros/domicilios/', cargar_registros_domicilios, name='cargar_registros_domicilios'),
    path('cargar_registros/eventos/', cargar_registros_eventos, name='cargar_registros_eventos'),

    #PARTIDO
    path('partido/', PartidoListView.as_view(), name='partido_list'),
    path('partido/add/', PartidoCreateView.as_view(), name='partido_create'),
    path('partido/update/<int:pk>/', PartidoUpdateView.as_view(), name='partido_update'),
    path('partido/delete/<int:pk>/', PartidoDeleteView.as_view(), name='partido_delete'),
]

