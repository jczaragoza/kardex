import json
from xml.dom.expatbuilder import CDATA_SECTION_NODE

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, View


#IMPORT MODEL AND FORM
from core.fichas.forms import OrganizacionForm, EventoForm, IntegranteForm
from core.fichas.models import Organizacion, Integrantes

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class OrganizacionListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Organizacion
    template_name = 'organizaciones/list.html'
    permission_required = 'view_organizacion'
    url_redirect = reverse_lazy('fichas:organizacion_list')

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for i in Organizacion.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Organizaciones'
        context['create_url'] = reverse_lazy('fichas:organizacion_create')
        context['list_url'] = reverse_lazy('fichas:organizacion_list')
        context['entity'] = 'Organizaciones'
        return context

class OrganizacionCreateView(PermissionMixin, CreateView):
    model = Organizacion
    template_name = 'organizaciones/create.html'
    form_class = OrganizacionForm
    success_url = reverse_lazy('fichas:organizacion_list')
    permission_required = 'add_organizacion'

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'nombre':
                if Organizacion.objects.filter(nombre=obj):
                    data['valid'] = False
        except:
            pass
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                form = OrganizacionForm(request.POST, request.FILES)
                data = form.save()
            elif action == 'add_evento':
                formEvento = EventoForm(request.POST)
                data = formEvento.save()
            elif action == 'add_integrante':
                formIntegrante = IntegranteForm(request.POST)
                data = formIntegrante.save()
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
        context['title'] = 'Nuevo registro Organización'
        context['titleEvento'] = 'Nuevo registro de evento'
        context['action'] = 'add'
        context['frmEvento'] = EventoForm()
        context['frmIntegrante'] = IntegranteForm()
        return context

class OrganizacionUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = Organizacion
    form_class = OrganizacionForm
    template_name = 'organizaciones/create.html'
    success_url = reverse_lazy('fichas:organizacion_list')
    permission_required = 'change_organizacion'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            elif action == 'add_evento':
                formEvento = EventoForm(request.POST)
                data = formEvento.save()
            elif action == 'add_integrante':
                formIntegrante = IntegranteForm(request.POST)
                data = formIntegrante.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualización de datos'
        context['entity'] = 'Organizaciones'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['frmEvento'] = EventoForm()
        context['frmIntegrante'] = IntegranteForm()
        context['titleEvento'] = 'Nuevo registro de evento'
        return context

class OrganizacionDeleteView(PermissionMixin, LoginRequiredMixin, DeleteView):
    model = Organizacion
    template_name = 'organizaciones/delete.html'
    success_url = reverse_lazy('fichas:organizacion_list')
    permission_required = 'delete_organizacion'
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
        context['title'] = 'Eliminación de Organizacion'
        context['entity'] = 'Organizacion'
        context['list_url'] = self.success_url
        return context

class OrganizacionDetailView(PermissionMixin, LoginRequiredMixin, DetailView):
    template_name = 'organizaciones/detail.html'
    queryset = Organizacion.objects.all()
    context_object_name = 'organizacion'
    permission_required = 'view_organizacion'
        
    def get_context_data(self, *args, **kwargs):
        # El pk que pasas a la URL
        pk = self.kwargs.get('pk')
        context = super(OrganizacionDetailView, self).get_context_data(**kwargs)
        return context


