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
from core.organizaciones.forms import OrganizacionForm
from core.organizaciones.models import Organizacion, FichaCurricular, Evento, Detalle

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class OrganizacionConsultaView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Organizacion
    template_name = 'consulta/consulta_organizaciones.html'
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
        context['title'] = 'Consulta en listado de Organizaciones Sociales'
        context['create_url'] = reverse_lazy('organizaciones:organizacion_create')
        context['list_url'] = reverse_lazy('organizaciones:organizacion_consulta')
        context['entity'] = 'Organizaciones'
        return context

class OrganizacionConsultaDetailView(PermissionMixin, LoginRequiredMixin, DetailView):
    template_name = 'consulta/detail_organizacion.html'
    queryset = Organizacion.objects.all()
    context_object_name = 'organizacion'
    permission_required = 'view_organizacion'
        
    def get_context_data(self, *args, **kwargs):
        # El pk que pasas a la URL
        pk = self.kwargs.get('pk')
        context = super(OrganizacionConsultaDetailView, self).get_context_data(**kwargs)
        context['detalles'] = Detalle.objects.filter(organizacion_id=pk)
        context['lideres'] = FichaCurricular.objects.filter(organizacion_id=self.kwargs['pk'])

        return context



