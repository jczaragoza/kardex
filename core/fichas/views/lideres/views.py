import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, View, TemplateView


#IMPORT MODEL AND FORM
from core.fichas.forms import LiderForm, EventoForm, DomicilioForm, TemasForm, VehiculoForm, ExperienciaForm, CargoForm
from core.fichas.models import Lider

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class LiderListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Lider
    template_name = 'lideres/list.html'
    permission_required = 'view_lider'
    url_redirect = reverse_lazy('fichas:lider_list')

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for i in Lider.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Líderes'
        context['create_url'] = reverse_lazy('fichas:lider_create')
        context['list_url'] = reverse_lazy('fichas:lider_list')
        context['entity'] = 'Lideres'
        return context

class LiderCreateView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = Lider
    template_name = 'lideres/create.html'
    form_class = LiderForm
    success_url = reverse_lazy('fichas:lider_list')
    permission_required = 'add_lider'

    def validate_data(self):
        data = {'valid': True}
        try:
            type = self.request.POST['type']
            obj = self.request.POST['obj'].strip()
            if type == 'nombre':
                if Lider.objects.filter(nombre=obj):
                    data['valid'] = False
            elif type == 'curp':
                if Lider.objects.filter(curp=obj):
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
            elif action == 'add_evento':
                formEvento = EventoForm(request.POST)
                data = formEvento.save()
            elif action == 'add_domicilio':
                formDomicilio = DomicilioForm(request.POST)
                data = formDomicilio.save()     
            elif action == 'add_vehiculo':
                formVehiculo = VehiculoForm(request.POST)
                data = formVehiculo.save()
            elif action == 'add_experiencia':
                formExperiencia = ExperienciaForm(request.POST)
                data = formExperiencia.save()                  
            elif action == 'add_cargo':
                formCargo = CargoForm(request.POST)
                data = formCargo.save()                     
            elif action == 'add_tema':
                formTemas = TemasForm(request.POST)
                data = formTemas.save()
            elif action == 'validate_data':
                return self.validate_data()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo Registro'
        context['action'] = 'add'
        context['titleModalEvento'] = 'Nuevo registro de evento'
        context['frmEvento'] = EventoForm()
        context['frmDomicilio'] = DomicilioForm()
        context['frmTemas'] = TemasForm()
        context['frmVehiculo'] = VehiculoForm()
        context['frmExperiencia'] = ExperienciaForm()
        context['frmCargo'] = CargoForm()
        return context

class LiderUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = Lider
    form_class = LiderForm
    template_name = 'lideres/update.html'
    success_url = reverse_lazy('fichas:lider_list')
    permission_required = 'change_lider'
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
            elif action == 'add_domicilio':
                formDomicilio = DomicilioForm(request.POST)
                data = formDomicilio.save()       
            elif action == 'add_vehiculo':
                formVehiculo = VehiculoForm(request.POST)
                data = formVehiculo.save()       
            elif action == 'add_tema':
                formTemas = TemasForm(request.POST)
                data = formTemas.save()
            elif action == 'add_experiencia':
                formExperiencia = ExperienciaForm(request.POST)
                data = formExperiencia.save()                  
            elif action == 'add_cargo':
                formCargo = CargoForm(request.POST)
                data = formCargo.save()                     
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualización de datos'
        context['entity'] = 'lider'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['titleModalEvento'] = 'Nuevo registro de evento'
        context['frmEvento'] = EventoForm()
        context['frmDomicilio'] = DomicilioForm()
        context['frmTemas'] = TemasForm()
        context['frmVehiculo'] = VehiculoForm()
        context['frmExperiencia'] = ExperienciaForm()
        context['frmCargo'] = CargoForm()
        return context

class LiderDeleteView(PermissionMixin, LoginRequiredMixin, DeleteView):
    model = Lider
    template_name = 'lideres/delete.html'
    success_url = reverse_lazy('fichas:lider_list')
    permission_required = 'delete_lider'
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
        context['title'] = 'Eliminación de Líder'
        context['entity'] = 'lider'
        context['list_url'] = self.success_url
        return context

class LiderDetailView(PermissionMixin, LoginRequiredMixin, DetailView):
    template_name = 'lideres/detail.html'
    queryset = Lider.objects.all()
    context_object_name = 'lider'
    permission_required = 'view_lider'
        
    def get_context_data(self, *args, **kwargs):
        # El pk que pasas a la URL
        pk = self.kwargs.get('pk')
        context = super(LiderDetailView, self).get_context_data(**kwargs)
        # context['detalles'] = Detalle.objects.filter(organizacion_id=pk)
        # context['lideres'] = FichaCurricular.objects.filter(organizacion_id=self.kwargs['pk'])

        return context


