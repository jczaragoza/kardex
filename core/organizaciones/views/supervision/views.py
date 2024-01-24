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

#Import model & form
from core.organizaciones.forms import OrganizacionForm, SupervisionOrganizacionForm
from core.organizaciones.models import Organizacion, FichaCurricular, Evento, Detalle

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class SupervisionListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Organizacion
    template_name = 'supervision/list.html'
    permission_required = 'view_organizacion'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for u in Organizacion.objects.all():
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Organizaciones'
        context['create_url'] = reverse_lazy('organizaciones:organizacion_create')
        context['list_url'] = reverse_lazy('organizaciones:organizacion_list')
        context['entity'] = 'Organizaciones'
        return context

class SupervisionReportes(PermissionMixin, ListView, LoginRequiredMixin):
    model = Organizacion
    template_name = 'supervision/reportes.html'
    permission_required = 'view_organizacion'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                search = Organizacion.objects.all()
                for s in search:
                    data.append([
                        s.nombre,
                        s.tipo_organizacion,
                        s.estatus_ficha,
                        s.get_user(),
                        s.modified.strftime('%Y-%m-%d'),
                    ])
                # for u in Organizacion.objects.all():
                #     data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Organizaciones'
        context['create_url'] = reverse_lazy('organizaciones:organizacion_create')
        context['list_url'] = reverse_lazy('organizaciones:supervision_reportes')
        context['entity'] = 'Organizaciones'
        return context

class SupervisionUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = Organizacion
    form_class = SupervisionOrganizacionForm
    template_name = 'supervision/create.html'
    success_url = reverse_lazy('organizaciones:supervision_list')
    permission_required = 'change_organizacion'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'correo':
                if Organizacion.objects.filter(correo=obj):
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
        context['entity'] = 'Organizaciones'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class SupervisionDetailView(PermissionMixin, LoginRequiredMixin, DetailView):
    template_name = 'supervision/detail.html'
    queryset = Organizacion.objects.all()
    context_object_name = 'organizacion'
    permission_required = 'view_organizacion'
        
    def get_context_data(self, *args, **kwargs):
        # El pk que pasas a la URL
        pk = self.kwargs.get('pk')
        context = super(SupervisionDetailView, self).get_context_data(**kwargs)
        context['detalles'] = Detalle.objects.filter(organizacion_id=pk)
        context['lideres'] = FichaCurricular.objects.filter(organizacion_id=self.kwargs['pk'])

        return context