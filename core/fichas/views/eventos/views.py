import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, View

#Import model & form
from core.fichas.forms import EventoForm
from core.fichas.models import Evento

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class EventoListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Evento
    template_name = 'evento/list.html'
    permission_required = 'view_evento'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for u in Evento.objects.all():
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Eventos'
        context['create_url'] = reverse_lazy('fichas:evento_create')
        context['list_url'] = reverse_lazy('fichas:evento_list')
        context['entity'] = 'Eventos'
        return context

class EventoCreateView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = Evento
    template_name = 'evento/create.html'
    form_class = EventoForm
    success_url = reverse_lazy('fichas:evento_list')
    permission_required = 'add_evento'

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'nombre':
                if Evento.objects.filter(nombre=obj):
                    data['valid'] = False
            elif type == 'descripcion':
                if Evento.objects.filter(descripcion=obj):
                    data['valid'] = False
            elif type == 'fecha_evento':
                if Evento.objects.filter(fecha_evento=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo Registro'
        context['action'] = 'add'
        return context

class EventoUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = Evento
    form_class = EventoForm
    template_name = 'evento/create.html'
    success_url = reverse_lazy('fichas:evento_list')
    permission_required = 'change_evento'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def validate_data(self):
        data = {'valid': True}
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
        context['entity'] = 'Eventos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

class EventoDeleteView(PermissionMixin, LoginRequiredMixin, DeleteView):
    model = Evento
    template_name = 'evento/delete.html'
    success_url = reverse_lazy('fichas:evento_list')
    permission_required = 'delete_evento'
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
        context['title'] = 'Eliminación de <evento'
        context['entity'] = 'Evento'
        context['list_url'] = self.success_url
        return context

