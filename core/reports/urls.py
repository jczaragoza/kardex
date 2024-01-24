from unicodedata import name
from django.urls import path
from core.reports.views.pdf.views import *

from django.conf.urls import include

app_name = 'reports'

urlpatterns = [
    #PDF
    path('pdf/<int:pk>/', ExportPDF.as_view(), name='export_pdf'),
    #PDF CANDIDATOS
    path('candidato/pdf/<int:pk>/', CandidatoExportPDF.as_view(), name='export_candidato_pdf'),
    path('organizacion/pdf/<int:pk>/', OrganizacionExportPDF.as_view(), name='export_organizacion_pdf'),
    path('lider/pdf/<int:pk>/', LiderExportPDF.as_view(), name='export_ficha_curricular_pdf'),
    
]
