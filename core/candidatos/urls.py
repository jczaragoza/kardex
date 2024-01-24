from django.urls import path

from core.candidatos.views.candidato.views import *
from core.candidatos.views.captura.views import *
from core.candidatos.views.partido.views import *
from core.candidatos.views.consulta.views import *
from core.candidatos.views.elecciones.views import *

from django.conf.urls import include

app_name = 'candidatos'

urlpatterns = [
    #CANDIDATO
    path('candidato/', CandidatoListView.as_view(), name='candidato_list'),
    path('add/', CandidatoCreateView.as_view(), name='candidato_create'),
    path('update/<int:pk>/', CandidatoUpdateView.as_view(), name='candidato_update'),
    path('delete/<int:pk>/', CandidatoDeleteView.as_view(), name='candidato_delete'),
    path('detail/<int:pk>/', CandidatoDetailView.as_view(), name='candidato_detail'),

    #ELECCIONES
    path('elecciones/', EleccionesListView.as_view(), name='elecciones_list'),

    # #PARTIDO
    # path('partido/', PartidoListView.as_view(), name='partido_list'),
    # path('partido/add/', PartidoCreateView.as_view(), name='partido_create'),
    # path('partido/update/<int:pk>/', PartidoUpdateView.as_view(), name='partido_update'),
    # path('partido/delete/<int:pk>/', PartidoDeleteView.as_view(), name='partido_delete'),
            
    #CONSULTA
    path('consulta/', CandidatoConsultaView.as_view(), name='candidato_consulta'),
    path('consulta/detail/<int:pk>/', CandidatoConsultaDetaillView.as_view(), name='consulta_detail_candidato'),
    path('consulta/update/<int:pk>/', CandidatoConsultaUpdateView.as_view(), name='consulta_update_candidato'),

    #CAPTURA
    path('captura/', CapturaListView.as_view(), name='captura_list'),
    path('captura/add/', CapturaCreateView.as_view(), name='captura_create'),
    path('captura/update/<int:pk>/', CapturaUpdateView.as_view(), name='captura_update'),
    path('captura/detail/<int:pk>/', CapturaDetailView.as_view(), name='captura_detail'),
]