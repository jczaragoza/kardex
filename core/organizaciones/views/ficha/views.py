import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, View

#Import model & form
from core.organizaciones.forms import FichaForm
from core.organizaciones.models import FichaCurricular, Detalle, Organizacion

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class FichaListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = FichaCurricular
    template_name = 'ficha/list.html'
    permission_required = 'view_fichacurricular'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for u in FichaCurricular.objects.all():
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Fichas de líderes sociales'
        context['create_url'] = reverse_lazy('organizaciones:ficha_create')
        context['list_url'] = reverse_lazy('organizaciones:ficha_list')
        context['entity'] = 'Fichas'
        return context

class FichaCreateView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = FichaCurricular
    template_name = 'ficha/create.html'
    form_class = FichaForm
    success_url = reverse_lazy('organizaciones:ficha_list')
    permission_required = 'add_evento'

    def validate_data(self):
        data = {'valid': True}
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
        context['title'] = 'Nuevo Registro de Líder'
        context['action'] = 'add'
        return context

class FichaUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = FichaCurricular
    form_class = FichaForm
    template_name = 'ficha/create.html'
    success_url = reverse_lazy('organizaciones:ficha_list')
    permission_required = 'change_fichacurricular'
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
        context['entity'] = 'FichaCurricular'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class FichaDeleteView(PermissionMixin, LoginRequiredMixin, DeleteView):
    model = FichaCurricular
    template_name = 'ficha/delete.html'
    success_url = reverse_lazy('organizaciones:ficha_list')
    permission_required = 'delete_fichacurricular'
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
        context['entity'] = 'FicchaCurricular'
        context['list_url'] = self.success_url
        return context


class FichaDetalleView(PermissionMixin, LoginRequiredMixin, DetailView):
    template_name = 'ficha/detail.html'
    queryset = FichaCurricular.objects.all()
    context_object_name = 'fichas'
    permission_required = 'view_fichacurricular'
        
    def get_context_data(self, *args, **kwargs):
        # El pk que pasas a la URL
        pk = self.kwargs.get('pk')
        context = super(FichaDetalleView, self).get_context_data(**kwargs)
        context['detalle_ficha'] = Detalle.objects.filter(fichacurricular_id=pk)

        return context