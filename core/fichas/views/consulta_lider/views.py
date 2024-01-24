import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, View

#Import model
from core.fichas.models import *

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class ConsultaLiderListView(PermissionMixin, ListView, LoginRequiredMixin):
    model = Lider
    template_name = 'consulta_lider/list.html'
    permission_required = 'view_lider'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'searchdata':
                data = []
                resultado = Lider.objects.filter(is_active = True)
                for u in resultado:
                    data.append(u.toJSON())
            else:
                data['error'] = 'No ha ingresado una opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Fichas de líderes sociales'
        context['create_url'] = reverse_lazy('fichas:lider_create')
        context['list_url'] = reverse_lazy('fichas:consulta_lider_list')
        context['entity'] = 'Fichas'
        return context

class ConsultaFichaDetalleView(PermissionMixin, LoginRequiredMixin, DetailView):
    template_name = 'consulta_lider/detail.html'
    queryset = Lider.objects.all()
    context_object_name = 'lider'
    permission_required = 'view_lider'
        
    def get_context_data(self, *args, **kwargs):
        # El pk que pasas a la URL
        pk = self.kwargs.get('pk')
        context = super(ConsultaFichaDetalleView, self).get_context_data(**kwargs)
        context['Hi'] = 'Say Yes!'

        return context