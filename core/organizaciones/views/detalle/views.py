import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, View

#Import model & form
from core.organizaciones.forms import DetalleForm, EventoForm
from core.organizaciones.models import Organizacion, Detalle, Evento, FichaCurricular

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class DetalleListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Detalle
    template_name = 'detalle/list.html'
    permission_required = 'view_detalle'
    
    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                for u in Detalle.objects.all():
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agenda Eventos'
        context['create_url'] = reverse_lazy('organizaciones:detalle_create')
        context['list_url'] = reverse_lazy('organizaciones:detalle_list')
        context['entity'] = 'Detalles'
        return context

class DetalleCreateView(PermissionMixin, LoginRequiredMixin, CreateView):
    model = Detalle
    form_class = DetalleForm
    template_name = 'detalle/create.html'
    success_url = reverse_lazy('organizaciones:detalle_list')
    permission_required = 'add_detalle'
    url_redirect = success_url
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def validate_data(self):
        data = {'valid': True}
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add_detalle':
                vents = json.loads(request.POST['vents'])
                detalle = Detalle()
                detalle.evento_id = vents['evento']
                detalle.organizacion_id = vents['organizacion']
                detalle.fichacurricular_id = vents['fichacurricular']
                detalle.save()
                data = {'id': detalle.id}
                #data = self.get_form().save()
            elif action == 'validate_data':
                return self.validate_data()
            elif action == 'autocomplete_org':
                data = []
                for i in Organizacion.objects.filter(nombre__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.nombre
                    data.append(item)
            elif action == 'search_evento':
                data = []
                for i in Evento.objects.filter(nombre__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
            elif action == 'search_lider':
                data = []
                for i in FichaCurricular.objects.filter(nombre__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)
            elif action == 'create_evento':
                frmEvento = EventoForm(request.POST)
                data = frmEvento.save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        #return JsonResponse(data, safe=False)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo registro'
        context['entity'] = 'Detalles'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['frmEvento'] = EventoForm()
        return context

class DetalleUpdateView(PermissionMixin, UpdateView, LoginRequiredMixin):
    model = Detalle
    form_class = DetalleForm
    template_name = 'detalle/create.html'
    success_url = reverse_lazy('organizaciones:detalle_list')
    permission_required = 'change_detalle'
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
            action = request.POST['action']
            if action == 'add_detalle':
                vents = json.loads(request.POST['vents'])
                detalle = Detalle()
                detalle.evento_id = vents['evento']
                detalle.organizacion_id = vents['organizacion']
                detalle.fichacurricular_id = vents['fichacurricular']
                detalle.save()
                data = {'id': detalle.id}
                #data = self.get_form().save()
            elif action == 'validate_data':
                return self.validate_data()
            elif action == 'autocomplete_org':
                data = []
                for i in Organizacion.objects.filter(nombre__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.nombre
                    data.append(item)
            elif action == 'search_evento':
                data = []
                for i in Evento.objects.filter(nombre__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.nombre
                    data.append(item)
            elif action == 'search_lider':
                data = []
                for i in FichaCurricular.objects.filter(nombre__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.nombre
                    data.append(item)
            elif action == 'create_evento':
                frmEvento = EventoForm(request.POST)
                data = frmEvento.save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        #return JsonResponse(data, safe=False)
        return HttpResponse(json.dumps(data), content_type='application/json')
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualización de datos'
        context['entity'] = 'Organizaciones'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context

class DetalleDeleteView(PermissionMixin, LoginRequiredMixin, DeleteView):
    model = Detalle
    template_name = 'detalle/delete.html'
    success_url = reverse_lazy('organizaciones:detalle_list')
    permission_required = 'delete_detalle'
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
        context['title'] = 'Eliminación de detalle'
        context['entity'] = 'Detalle'
        context['list_url'] = self.success_url
        return context

