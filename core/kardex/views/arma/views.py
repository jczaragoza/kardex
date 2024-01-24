from contextlib import ContextDecorator
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from core.kardex.forms import ArmaForm, PersonaForm, CursoForm, VehiculoForm
from core.kardex.models import Cursos, Persona, Vehiculos, Armas

#Mixins
from core.security.mixins import PermissionMixin

from core.security.models import *

class ArmaListView(ListView, PermissionMixin, LoginRequiredMixin):
    model = Armas
    template_name = 'arma/list.html'
    permission_required = 'view_arma'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for u in Armas.objects.all():
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de armas'
        context['create_url'] = reverse_lazy('kardex:arma_create')
        context['list_url'] = reverse_lazy('kardex:arma_list')
        context['entity'] = 'Armas'
        return context

class ArmaCreateView(LoginRequiredMixin, CreateView, PermissionMixin):
    model = Armas
    form_class = ArmaForm
    template_name = 'arma/create.html'
    success_url = reverse_lazy('kardex:arma_list')
    permission_required = 'add_arma'
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
        context['title'] = 'Alta de Arma'
        context['entity'] = 'Armas'
        context['create_url'] = reverse_lazy('kardex:arma_create')
        context['list_url'] = reverse_lazy('kardex:arma_list')
        context['action'] = 'add'
        return context

class ArmaUpdateView(LoginRequiredMixin, UpdateView, PermissionMixin):
    model = Armas
    form_class = ArmaForm
    template_name = 'arma/create.html'
    success_url = reverse_lazy('kardex:arma_list')
    permission_required = 'change_arma'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                data = self.get_form().save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualización de datos'
        context['entity'] = 'Armas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

class ArmaDeleteView(LoginRequiredMixin, DeleteView, PermissionMixin):
    model = Armas
    template_name = 'arma/delete.html'
    success_url = reverse_lazy('kardex:arma_list')
    permission_required = 'delete_arma'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de arma'
        context['entity'] = 'Armas'
        context['list_url'] = self.success_url
        return context
