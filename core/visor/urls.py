from unicodedata import name
from django.urls import path
from core.visor.views import *

from django.conf.urls import include

app_name = 'visor'

urlpatterns = [
    #visor
    path('geocode/', VisorView.as_view(), name='visor_main'),
]
