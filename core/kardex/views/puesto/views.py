import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from core.kardex.forms import PersonaForm, CursoForm, PuestoForm, VehiculoForm
from core.kardex.models import Cursos, Persona, Vehiculos, Puestos

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class PuestoListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Puestos
    template_name = 'puesto/list.html'
    permission_required = 'view_puestos'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for u in Puestos.objects.all():
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de puestos'
        context['create_url'] = reverse_lazy('kardex:puesto_create')
        context['list_url'] = reverse_lazy('kardex:puesto_list')
        context['entity'] = 'Puestos'
        return context


class PuestoCreateView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = Puestos
    form_class = PuestoForm
    template_name = 'puesto/create.html'
    success_url = reverse_lazy('kardex:puesto_list')
    permission_required = 'add_puestos'
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
        context['title'] = 'Alta de Puesto'
        context['entity'] = 'Puestos'
        context['create_url'] = reverse_lazy('kardex:puesto_create')
        context['list_url'] = reverse_lazy('kardex:puesto_list')
        context['action'] = 'add'
        return context

class PuestoUpdateView(PermissionMixin, LoginRequiredMixin, UpdateView):
    model = Puestos
    form_class = PuestoForm
    template_name = 'puesto/create.html'
    success_url = reverse_lazy('kardex:puesto_list')
    permission_required = 'change_puestos'
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
        context['entity'] = 'Puestos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context