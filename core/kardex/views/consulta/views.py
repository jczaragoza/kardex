from contextlib import ContextDecorator
from contextvars import Context
import json
import os

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
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from core.kardex.forms import PersonaForm, CursoForm

from core.kardex.models import Armas, Cursos, Persona, Vehiculos

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class PersonaAddView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'consulta/create.html'
    success_url = reverse_lazy('kardex:persona_consulta')
    permission_required = 'add_persona'
    
    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'clavesp':
                if Persona.objects.filter(clavesp=obj):
                    data['valid'] = False
            elif type == 'rfc':
                if Persona.objects.filter(rfc=obj):
                    data['valid'] = False
            elif type == 'curp':
                if Persona.objects.filter(curp=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Alta de Personal'
        context['entity'] = 'Personas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class PersonaConsultaView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Persona
    template_name = 'consulta/list.html'
    permission_required = 'view_persona'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for u in Persona.objects.all():
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Personal DGI'
        context['create_url'] = reverse_lazy('kardex:persona_create')
        context['list_url'] = reverse_lazy('kardex:persona_list')
        context['entity'] = 'Personas'
        context['activo'] = Persona.objects.filter(estatus = 'Activo')
        context['personal_uac'] = Persona.objects.filter(adscripcion = 3, estatus = 'Activo')
        context['personal_uiip'] = Persona.objects.filter(adscripcion = 1, estatus = 'Activo')

        return context

class ConsultaDetailView(PermissionMixin, LoginRequiredMixin, DetailView):
    template_name = 'consulta/detail.html'
    queryset = Persona.objects.all()
    context_object_name = 'persona'
    permission_required = 'view_persona'
    
    def get_context_data(self, *args, **kwargs):
        # El pk que pasas a la URL
        pk = self.kwargs.get('pk')
        context = super(ConsultaDetailView, self).get_context_data(**kwargs)
        context['cursos'] = Cursos.objects.filter(persona_id=pk)
        context['vehiculos'] = Vehiculos.objects.filter(persona_id = pk)
        context['armas'] = Armas.objects.filter(persona_id = pk)
        return context

class ConsultaUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = Persona
    form_class = PersonaForm
    template_name = 'consulta/create.html'
    success_url = reverse_lazy('kardex:persona_list')
    permission_required = 'change_persona'
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
            if type == 'clavesp':
                if Persona.objects.filter(dni=obj).exclude(id=id):
                    data['valid'] = False
            elif type == 'rfc':
                if Persona.objects.filter(rfc=obj).exclude(id=id):
                    data['valid'] = False
            elif type == 'curp':
                if Persona.objects.filter(curp=obj).exclude(id=id):
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
        context['entity'] = 'Personas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
