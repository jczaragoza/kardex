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

from core.candidatos.forms import CandidatoForm, CapturaForm

from core.candidatos.models import Candidato, Distrito_local, Distrito_local_cabeceras, Distrito_federal_municipios, Municipio
#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class CapturaListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Candidato
    template_name = 'captura/list.html'
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
        context['title'] = 'Listado de Actores Sociales'
        context['create_url'] = reverse_lazy('candidatos:captura_create')
        context['list_url'] = reverse_lazy('candidatos:captura_list')
        context['entity'] = 'candidato'
        return context

class CapturaCreateView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = Candidato
    form_class = CapturaForm
    template_name = 'captura/create.html'
    success_url = reverse_lazy('candidatos:candidato_list')
    permission_required = 'add_candidato'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Alta de Candidato'
        context['entity'] = 'Candidatos'
        context['create_url'] = reverse_lazy('candidatos:captura_create')
        context['list_url'] = reverse_lazy('candidatos:captura_list')
        context['action'] = 'add'
        return context

class CapturaUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = Candidato
    form_class = CapturaForm
    template_name = 'captura/create.html'
    success_url = reverse_lazy('candidatos:captura_list')
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
        context['entity'] = 'candidatos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

class CapturaDetailView(PermissionMixin, LoginRequiredMixin, DetailView):
    template_name = 'captura/detail.html'
    queryset = Candidato.objects.all()
    context_object_name = 'candidato'
    permission_required = 'view_candidato'
        
    def get_context_data(self, *args, **kwargs):
        # El pk que pasas a la URL
        context = super(CapturaDetailView, self).get_context_data(**kwargs)
        #context['candidato'] = Candidato.objects.get(pk=self.kwargs['pk'])
        context['distritos_locales'] = Distrito_local_cabeceras.objects.all()
        context['distritos_federales'] = Distrito_federal_municipios.objects.all()
        context['municipios'] = Municipio.objects.all()
        return context



