import json
import os

from django.conf import settings
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse_lazy

from django.views.generic import View
from weasyprint import HTML, CSS
from core.kardex.models import *
from core.candidatos.models import *
from core.fichas.models import *

from django.template.loader import render_to_string
from django.template.loader import get_template

#Mixins
from core.security.mixins import PermissionMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from core.security.models import *

# PDF KARDEX
class ExportPDF(LoginRequiredMixin, View):
    permission_required = 'view_persona', 'view_cursos'
    
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        persona = Persona.objects.get(pk=self.kwargs['pk'])
        curso = Cursos.objects.filter(persona_id=pk)
        arma = Armas.objects.filter(persona_id=pk)
        vehiculo = Vehiculos.objects.filter(persona_id=pk)
        bienes = Bienes.objects.filter(resguardatario_id=pk)
        
        html = render_to_string('pdf/file.html',
                            {
                                'persona': persona,
                                'cursos': curso,
                                'vehiculos': vehiculo,
                                'armas': arma,
                                'bienes': bienes,
                            })
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'filename=persona_{persona.id}.pdf'
        css_url = os.path.join(settings.BASE_DIR, 'static/lib/bootstrap-4.6.0/css/bootstrap.min.css')
        
        pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
        return HttpResponse(pdf, content_type='application/pdf')
     
class CandidatoExportPDF(LoginRequiredMixin, View):
    permission_required = 'view_candidato'
    
    def get(self, request, *args, **kwargs):
       
        candidato = Candidato.objects.get(pk=self.kwargs['pk'])
        distritos_locales = Distrito_local_cabeceras.objects.all()
        distritos_federales = Distrito_federal_municipios.objects.all()
        municipios = Municipio.objects.all()
        html = render_to_string('pdf/candidato.html',
                            {
                                'candidato': candidato,
                                'distritos_locales': distritos_locales,
                                'distritos_federales': distritos_federales,
                                'municipios': municipios,
                            })
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'filename=candidato_{candidato.id}.pdf'
        css_url = os.path.join(settings.BASE_DIR, 'static/lib/bootstrap-4.6.0/css/bootstrap.min.css')
        
        pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
        return HttpResponse(pdf, content_type='application/pdf')
      
class OrganizacionExportPDF(LoginRequiredMixin, View):
    permission_required = 'view_organizacion'
    
    def get(self, request, *args, **kwargs):
        
        organizacion = Organizacion.objects.get(pk=self.kwargs['pk'])
        html = render_to_string('pdf/organizacion.html',
                            {
                                'organizacion': organizacion,
                            })
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'filename=organizacion_{organizacion.id}.pdf'
        css_url = os.path.join(settings.BASE_DIR, 'static/lib/bootstrap-4.6.0/css/bootstrap.min.css')
        
        pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
        return HttpResponse(pdf, content_type='application/pdf')

class LiderExportPDF(LoginRequiredMixin, View):
    permission_required = 'view_lider'
    
    def get(self, request, *args, **kwargs):
        
        lider = Lider.objects.get(pk=self.kwargs['pk'])
        html = render_to_string('pdf/ficha_curricular.html',
                            {
                                'lider': lider,
                            })
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'filename=ficha_{lider.id}.pdf'
        css_url = os.path.join(settings.BASE_DIR, 'static/lib/bootstrap-4.6.0/css/bootstrap.min.css')
        
        pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
        return HttpResponse(pdf, content_type='application/pdf')
    