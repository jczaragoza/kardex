from django.urls import path
from core.dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    #REPORTES
    path('main/', DashMainView.as_view(), name='dash_main'),
    
]
