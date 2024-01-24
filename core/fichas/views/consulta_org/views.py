import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

#Import model
from core.fichas.models import *
#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class OrganizacionConsultaView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Organizacion
    template_name = 'consulta_org/list.html'
    permission_required = 'view_organizacion'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                resultado = Organizacion.objects.filter(is_active = True)
                for u in resultado:
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta en listado de Organizaciones Sociales'
        context['create_url'] = reverse_lazy('organizaciones:organizacion_create')
        context['list_url'] = reverse_lazy('organizaciones:consulta_org_list')
        context['entity'] = 'Organizaciones'
        return context

class OrganizacionConsultaDetailView(PermissionMixin, LoginRequiredMixin, DetailView):
    template_name = 'consulta_org/detail.html'
    queryset = Organizacion.objects.all()
    context_object_name = 'organizacion'
    permission_required = 'view_organizacion'
        
    def get_context_data(self, *args, **kwargs):
        # El pk que pasas a la URL
        pk = self.kwargs.get('pk')
        context = super(OrganizacionConsultaDetailView, self).get_context_data(**kwargs)
        context['Hi'] = 'Say Yes!'

        return context



