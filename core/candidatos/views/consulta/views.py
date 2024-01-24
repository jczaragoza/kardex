from contextlib import ContextDecorator
from contextvars import Context
import json
import os
from xml.dom.expatbuilder import CDATA_SECTION_NODE

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, View

from core.candidatos.forms import CandidatoForm

from core.candidatos.models import Candidato, Distrito_local, Distrito_local_cabeceras, Distrito_federal_municipios, Municipio
#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class CandidatoConsultaView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Candidato
    template_name = 'consulta_candidato/list_consulta.html'
    permission_required = 'view_candidato'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                resultado = Candidato.objects.filter(is_active=True)
                for u in resultado:
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de actores con cargo de elección popular' 
        context['create_url'] = reverse_lazy('candidatos:candidato_add')
        context['list_url'] = reverse_lazy('candidatos:candidato_consulta')
        context['entity'] = 'Candidatos'
        return context

class CandidatoConsultaDetaillView(PermissionMixin, LoginRequiredMixin, DetailView):
    template_name = 'consulta_candidato/detail.html'
    queryset = Candidato.objects.all()
    context_object_name = 'candidato'
    permission_required = 'view_candidato'
        
    def get_context_data(self, *args, **kwargs):
        # El pk que pasas a la URL
        context = super(CandidatoConsultaDetaillView, self).get_context_data(**kwargs)
        #context['candidato'] = Candidato.objects.get(pk=self.kwargs['pk'])
        context['distritos_locales'] = Distrito_local_cabeceras.objects.all()
        context['distritos_federales'] = Distrito_federal_municipios.objects.all()
        context['municipios'] = Municipio.objects.all()
        return context

class CandidatoConsultaUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = Candidato
    form_class = CandidatoForm
    template_name = 'consulta_candidato/create.html'
    success_url = reverse_lazy('candidatos:candidato_consulta')
    permission_required = 'change_candidato'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            id = self.get_object().id
            obj = self.request.POST['obj'].strip()
            if type == 'rfc':
                if Candidato.objects.filter(rfc=obj).exclude(id=id):
                    data['valid'] = False
            elif type == 'curp':
                if Candidato.objects.filter(curp=obj).exclude(id=id):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualización de datos'
        context['entity'] = 'Candidatos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context