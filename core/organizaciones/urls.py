from django.urls import path

from core.organizaciones.views.organizaciones.views import *
from core.organizaciones.views.supervision.views import *
from core.organizaciones.views.captura_org.views import *
from core.organizaciones.views.evento.views import *
from core.organizaciones.views.detalle.views import *
from core.organizaciones.views.ficha.views import *
from core.organizaciones.views.consulta.views import *
from core.organizaciones.views.consulta_lider.views import  *

from django.conf.urls import include

app_name = 'organizaciones'

urlpatterns = [
    #Organizaciones
    path('organizacion/', OrganizacionListView.as_view(), name='organizacion_list'),
    path('add/', OrganizacionCreateView.as_view(), name='organizacion_create'),
    path('update/<int:pk>/', OrganizacionUpdateView.as_view(), name='organizacion_update'),
    path('delete/<int:pk>/', OrganizacionDeleteView.as_view(), name='candidato_delete'),
    path('detail/<int:pk>/', OrganizacionDetailView.as_view(), name='organizacion_detail'),

    #Captura_Organizaciones
    path('org/', OrgListView.as_view(), name='org_list'),
    path('add_org/', OrgCreateView.as_view(), name='org_create'),
    path('update_org/<int:pk>/', OrgUpdateView.as_view(), name='org_update'),
    path('detail_org/<int:pk>/', OrgDetailView.as_view(), name='org_detail'),

    # #EVENTO
    # path('evento/', EventoListView.as_view(), name='evento_list'), 
    # path('evento/add/', EventoCreateView.as_view(), name='evento_create'),
    # path('evento/update/<int:pk>/', EventoUpdateView.as_view(), name='evento_update'),
    # path('evento/delete/<int:pk>/', EventoDeleteView.as_view(), name='evento_delete'),

    #FICHA_CURRICULAR
    path('ficha/', FichaListView.as_view(), name='ficha_list'), 
    path('ficha/add/', FichaCreateView.as_view(), name='ficha_create'),
    path('ficha/update/<int:pk>/', FichaUpdateView.as_view(), name='ficha_update'),
    path('ficha/detalle/<int:pk>/', FichaDetalleView.as_view(), name='ficha_detail'),
    path('ficha/delete/<int:pk>/', FichaDeleteView.as_view(), name='ficha_delete'),

    #DETALLE
    path('detalle/', DetalleListView.as_view(), name='detalle_list'), 
    path('detalle/add/', DetalleCreateView.as_view(), name='detalle_create'),
    path('detalle/update/<int:pk>/', DetalleUpdateView.as_view(), name='detalle_update'),
    path('detalle/delete/<int:pk>/', DetalleDeleteView.as_view(), name='detalle_delete'),

    #SUPERVISION
    path('supervision/', SupervisionListView.as_view(), name='supervision_list'), 
    path('reportes/', SupervisionReportes.as_view(), name='supervision_reportes'),
    path('supervision/update/<int:pk>/', SupervisionUpdateView.as_view(), name='supervision_update'),
    path('supervision/detail/<int:pk>/', SupervisionDetailView.as_view(), name='supervision_detail'),

    #CONSULTA
    path('consulta/', OrganizacionConsultaView.as_view(), name='organizacion_consulta'),
    path('consulta/detail/<int:pk>/', OrganizacionConsultaDetailView.as_view(), name='consulta_detail'),
    path('consulta_lider/', ConsultaLiderListView.as_view(), name='lider_consulta'),
    path('consulta_lider/detail/<int:pk>/', ConsultaFichaDetalleView.as_view(), name='consulta_lider'),


]