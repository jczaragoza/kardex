import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from core.kardex.forms import PersonaForm, CursoForm, VehiculoForm, BienesForm
from core.kardex.models import Cursos, Persona, Vehiculos, Bienes

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class BienesListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Bienes
    template_name = 'bienes/list.html'
    permission_required = 'view_bienes'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for u in Bienes.objects.all():
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Bienes'
        context['create_url'] = reverse_lazy('kardex:bienes_create')
        context['list_url'] = reverse_lazy('kardex:bienes_list')
        context['entity'] = 'Bienes'
        return context

class BienesCreateView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = Bienes
    form_class = BienesForm
    template_name = 'bienes/create.html'
    success_url = reverse_lazy('kardex:bienes_list')
    permission_required = 'add_bienes'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'resguardo':
                if Bienes.objects.filter(resguardo=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

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
        context['title'] = 'Alta de Bienes'
        context['entity'] = 'Bienes'
        context['create_url'] = reverse_lazy('kardex:bienes_create')
        context['list_url'] = reverse_lazy('kardex:bienes_list')
        context['action'] = 'add'
        return context

class BienesUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = Bienes
    form_class = BienesForm
    template_name = 'bienes/create.html'
    success_url = reverse_lazy('kardex:bienes_list')
    permission_required = 'change_bienes'
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
        context['entity'] = 'Bienes'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

class BienesDeleteView(PermissionMixin, LoginRequiredMixin, DeleteView):
    model = Bienes
    template_name = 'bienes/delete.html'
    success_url = reverse_lazy('kardex:bienes_list')
    permission_required = 'delete_bienes'
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
        context['title'] = 'Eliminación de Bien'
        context['entity'] = 'Bienes'
        context['list_url'] = self.success_url
        return context
