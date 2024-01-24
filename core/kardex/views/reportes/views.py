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
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, View

from core.kardex.forms import PersonaForm
from core.kardex.report_form import ReportForm

from core.kardex.models import Armas, Cursos, Persona, Vehiculos, Bienes

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class ReportesListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Persona
    template_name = 'reportes/persona.html'
    permission_required = 'view_persona'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'search_report':
                # data = []
                # for u in Persona.objects.all():
                #     data.append(u.toJSON())
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Persona.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_alta__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.get_full_name(),
                        s.clavesp,
                        s.get_puesto(),
                        s.fecha_alta.strftime('%Y-%m-%d'),
                        s.fecha_nacimiento.strftime('%Y-%m-%d'),
                        s.modified.strftime('%Y-%m-%d'),
                        s.get_adscripcion(),
                    ])
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
        context['form'] = ReportForm()
        context['entity'] = 'Personas'
        return context