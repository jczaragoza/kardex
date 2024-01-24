import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from core.candidatos.forms import PartidoForm
from core.candidatos.models import Candidato, Partido

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class PartidoListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Partido
    template_name = 'partido/list.html'
    permission_required = 'view_partido'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for u in Partido.objects.all():
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Partidos políticos'
        context['create_url'] = reverse_lazy('candidatos:partido_create')
        context['list_url'] = reverse_lazy('candidatos:partido_list')
        context['entity'] = 'Partidos'
        return context

class PartidoCreateView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = Partido
    form_class = PartidoForm
    template_name = 'partido/create.html'
    success_url = reverse_lazy('candidatos:partido_list')
    permission_required = 'add_partido'
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
        context['title'] = 'Alta de Partido'
        context['entity'] = 'Partidos'
        context['create_url'] = reverse_lazy('candidatos:partido_create')
        context['list_url'] = reverse_lazy('candidatos:partido_list')
        context['action'] = 'add'
        return context

class PartidoUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = Partido
    form_class = PartidoForm
    template_name = 'partido/create.html'
    success_url = reverse_lazy('candidatos:partido_list')
    permission_required = 'change_partido'
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
        context['entity'] = 'Partidos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

class PartidoDeleteView(PermissionMixin, LoginRequiredMixin, DeleteView):
    model = Partido
    template_name = 'partido/delete.html'
    success_url = reverse_lazy('candidatos:partido_list')
    permission_required = 'delete_partido'
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
        context['title'] = 'Eliminación de Partido'
        context['entity'] = 'Partidos'
        context['list_url'] = self.success_url
        return context
