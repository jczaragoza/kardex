import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.kardex.forms import CursoForm
from core.kardex.models import Cursos, Persona

from core.security.mixins import PermissionMixin, ModuleMixin

# QUERY
from django.db.models.query_utils import Q

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class CursoListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Cursos
    template_name = 'curso/list.html'
    permission_required = 'view_cursos'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for u in Cursos.objects.all():
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de cursos'
        context['create_url'] = reverse_lazy('kardex:curso_create')
        context['list_url'] = reverse_lazy('kardex:curso_list')
        context['entity'] = 'Cursos'
        return context


class CursoCreateView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = Cursos
    form_class = CursoForm
    template_name = 'curso/create.html'
    success_url = reverse_lazy('kardex:curso_list')
    permission_required = 'add_cursos'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_personas':
                data = []
                term = request.POST['term']
                personas = Persona.objects.filter(Q(clavesp__icontains = term) | Q(rfc__icontains = term) | Q(apaterno__icontains = term) | Q(amaterno__icontains = term) | Q(nombre__icontains = term))[0:10]
                for i in personas:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
            elif action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Curso'
        context['entity'] = 'Cursos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class CursoUpdateView(PermissionMixin, LoginRequiredMixin, UpdateView):
    model = Cursos
    form_class = CursoForm
    template_name = 'curso/create.html'
    success_url = reverse_lazy('kardex:curso_list')
    permission_required = 'change_cursos'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición del Curso'
        context['entity'] = 'Cursos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class CursosDeleteView(PermissionMixin, LoginRequiredMixin, DeleteView):
    model = Cursos
    template_name = 'curso/delete.html'
    success_url = reverse_lazy('kardex:curso_list')
    permission_required = 'delete_cursos'
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
        context['title'] = 'Eliminación del Curso'
        context['entity'] = 'Cursos'
        context['list_url'] = self.success_url
        return context
