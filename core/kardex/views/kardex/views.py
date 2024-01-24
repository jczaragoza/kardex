from ast import Delete
import json
from site import check_enableusersite
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from core.kardex.forms import CursoForm, KardexForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from core.kardex.models import Cursos, Kardex, Persona


# QUERY
from django.db.models.query_utils import Q

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *


class KardexCreateView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = Kardex
    form_class = KardexForm
    template_name = 'kardex/create.html'
    success_url = reverse_lazy('kardex:kardex_list')
    permission_required = 'add_kardex'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_personas':
                data = []
                term = request.POST['term']
                personas = Persona.objects.filter(Q(clavesp__icontains = term) | Q(rfc__icontains = term) | Q(apaterno__icontains = term) | Q(amaterno__icontains = term) | Q(nombre__icontains = term))
                for i in personas:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
                # data = []
                # for i in Persona.objects.filter(nombre__icontains=request.POST['term'])[0:1]:
                #     item = i.toJSON()
                #     item['value'] = i.nombre
                #     data.append(item)
            elif action == 'add':
                kardex = json.loads(request.POST['kar'])
                kardex_aux = Kardex()
                kardex_aux.fecha_actual = kardex['fecha_actual']
                kardex_aux.curso_id = kardex['curso']
                
                for i in kardex['personas']:
                    kardex_aux.persona_id = i['id']
                    kardex_aux.save()
                    data = {'id': kardex_aux.id}

            elif action == 'search_cursos':
                data = []
                term = request.POST['term']
                cursos = Cursos.objects.filter(Q(nombre__icontains = term) | Q(id__icontains = term))
                for i in cursos:
                    item = i.toJSON()
                    item['text'] = i.nombre
                    data.append(item)
            elif action == 'create_curso':
                frmCurso = CursoForm(request.POST)
                data = frmCurso.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Kardex'
        context['entity'] = 'Kardex'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['frmCurso'] = CursoForm 
        return context


class KardexListView(PermissionMixin, LoginRequiredMixin, ListView):
    model = Kardex
    template_name = 'kardex/list.html'
    permission_required = 'view_kardex'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Kardex.objects.all():
                    data.append(i.toJSON())
            # elif action == 'search_details_persona':
            #     data = []
            #     for i in detKardex.objects.filter(kardex_id=request.POST['id']):
            #         data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Kardex'
        context['create_url'] = reverse_lazy('kardex:kardex_create')
        context['list_url'] = reverse_lazy('kardex:kardex_list')
        context['entity'] = 'Kardex'
        return context


class kardexDeleteView(PermissionMixin, LoginRequiredMixin, DeleteView):
    model = Kardex
    template_name = 'kardex/delete.html'
    success_url = reverse_lazy('kardex:kardex_list')
    permission_required = 'delete_kardex'
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
        context['title'] = 'Eliminación de un Kardex'
        context['entity'] = 'Kardex'
        context['list_url'] = self.success_url
        return context