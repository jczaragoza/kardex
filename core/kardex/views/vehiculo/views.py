import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from core.kardex.forms import PersonaForm, CursoForm, VehiculoForm
from core.kardex.models import Cursos, Persona, Vehiculos

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class VehiculoListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Vehiculos
    template_name = 'vehiculo/list.html'
    permission_required = 'view_vehiculos'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for u in Vehiculos.objects.all():
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Vehículos'
        context['create_url'] = reverse_lazy('kardex:vehiculo_create')
        context['list_url'] = reverse_lazy('kardex:vehiculo_list')
        context['entity'] = 'Vehiculos'
        return context

class VehiculoCreateView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = Vehiculos
    form_class = VehiculoForm
    template_name = 'vehiculo/create.html'
    success_url = reverse_lazy('kardex:vehiculo_list')
    permission_required = 'add_vehiculos'
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
        context['title'] = 'Alta de Vehículo'
        context['entity'] = 'Vehiculos'
        context['create_url'] = reverse_lazy('kardex:vehiculo_create')
        context['list_url'] = reverse_lazy('kardex:vehiculo_list')
        context['action'] = 'add'
        return context

class VehiculoUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = Vehiculos
    form_class = VehiculoForm
    template_name = 'vehiculo/create.html'
    success_url = reverse_lazy('kardex:vehiculo_list')
    permission_required = 'change_vehiculos'
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
        context['entity'] = 'Vehículos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

class VehiculoDeleteView(PermissionMixin, LoginRequiredMixin, DeleteView):
    model = Vehiculos
    template_name = 'vehiculo/delete.html'
    success_url = reverse_lazy('kardex:vehiculo_list')
    permission_required = 'delete_vehiculos'
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
        context['title'] = 'Eliminación de Vehículo'
        context['entity'] = 'Vehículos'
        context['list_url'] = self.success_url
        return context
