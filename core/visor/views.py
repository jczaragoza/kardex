from django.shortcuts import render

# Create your views here.
from contextlib import ContextDecorator
from contextvars import Context
import json
import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView, TemplateView

#Mixins
from core.security.mixins import PermissionMixin
from core.security.models import *

class VisorView(LoginRequiredMixin, TemplateView): 
    template_name = 'visor/visor.html'